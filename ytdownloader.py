#!/usr/bin/env python3

# Coded By f4ll_py
# Re-written by @arcticlimer

"""
Main application module.
The main function runs a while 
window loop and parse his events
"""

import pytube
import urllib

from typing import Union
from typing import Tuple

from youtube import YouTube
from youtube import Playlist
from window import Window


def main() -> None:

    youtube = None
    playlist = None
    
    # Main window loop
    while not window.is_closed:

        event, values = window.read()

        stream = values['stream']
        path = values['path']
        url = values['url']

        if event == 'search':
            # Cleaning last search objects
            youtube = None
            playlist = None

            youtube, playlist = search(url=url,
                                       path=path)

        if event == 'Download':
            download(youtube=youtube,
                     playlist=playlist,
                     stream=stream,
                     path=path)

    window.close()


def handle_exceptions(func):
    """
    This is needed since pytube current version is 
    quite unstable and can raise some unexpected errors.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except KeyError as e:
            window.s_append('An error with the cipher has ocurred. '
                            'See documentation in GitHub to resolve: '
                            'https://github.com/f4ll-py/ytdownloader.')

        except pytube.exceptions.RegexMatchError:
            window.s_append('Could not find any YouTube videos with that URL.')

        except urllib.error.HTTPError:
            window.s_append('This video is not available. Try again later.')

        except PermissionError:
            window.s_append('Permission denied for the current path.')

    return wrapper


@handle_exceptions
def search(url:    str,
           path:   str,) -> Tuple[Union[YouTube, None],
                                  Union[Playlist, None]]:
    """
    
    """
    window.s_append(f'Searching for {url}...')

    youtube = playlist = None

    if 'playlist?' in url:
        playlist = Playlist(url=url,
                            window=window)

        window.s_append('Playlist found! Select a download mode on '
                        'the streams below!')

        window['stream'].update(values=['Video (Max quality)',
                                        'Audio (Max quality)'])

    else:

        youtube = YouTube(path=path,
                          url=url,
                          window=window)

        v = [f'{v.resolution} ({v.fps} FPS)' for v in youtube['videos']]
        a = [a.abr for a in youtube['audios']]

        window['stream'].update(values=v+a)

        window.s_append(f'{len(youtube)} downloadable streams found!' 
                        ' Select one below!')

    return youtube, playlist


@handle_exceptions
def download(youtube : Union[YouTube, None],
             playlist: Union[Playlist, None],
             stream:   str,
             path:     str):
    """
    
    """

    if not playlist and not youtube:
        window.s_append('You must search for a video before download!')
        return

    if playlist:

        for video_url in playlist.video_urls:

            # A try here is needed since it would
            # stop downloading the playlist after
            # an exception. 
            try:

                youtube = YouTube(path=path,
                                  url=video_url,
                                  window=window)

                if 'Audio' in stream:
                    youtube.download_audio(title=True)

                else:
                    youtube.download_video()

            except Exception as e:
                window.s_append('An unexpected pytube library error occured,'
                                ' could not download.')
                print(f'Exception {e}')

        window.s_append('All downloads finished!')

    else:
        quality = stream[:5].strip()
        fps = int(stream[-7:-5])

        if 'kb' in quality:
            youtube.download_audio(bitrate=stream)

        else:
            youtube.download_video(res=quality,
                                   fps=fps)

        window.s_append(f'{youtube.title} download finished!')


if __name__ == '__main__':
    window = Window(theme='SystemDefault1',
                    justify='left',
                    font=('Calibri', 12),
                    button=('Black', 'White'))
    main()
