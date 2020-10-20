
"""
Module that wraps pytube objects.
pytube.YouTube and pytube.Playlist
are wrapped here into the YouTube
and Playlist classes for easier usage.

This modules requires ffmpeg installed to work.
"""

import subprocess
import datetime
import time
import os
import re

import pytube

from pathlib import Path
from typing import List
from typing import Union

from window import Window


FFMPEG_CMD = 'ffmpeg -y -i {0._video_path} -i {0._audio_path} ' \
             '-c:v copy -c:a aac -map 0:v:0 -map 1:a:0 {0.path}/{0._title}.mp4'

RESOLUTIONS = ['2160p', '1440p', '1080p', '720p',
               '480p', '360p', '240p', '144p']


class YouTube(pytube.YouTube):
    """
    Youtube class. Inherits from pytube.YouTube.
    
    Parameters
    ----------
    path : `str`
        Path where the videos/audios will be downloaded
    
    url : `str`
        Video to download url's
    
    window : `Window`
        Window object used for controlling it status
    """
    def __init__(self,
                 path:   str,
                 url:    str,
                 window: Window) -> None:

        super().__init__(url=url)

        length = str(datetime.timedelta(seconds=self.length))

        window.update_header(f'\nTitle: {self.title}',
                      f'Author: {self.author}',
                      f'Length: {length}')

        self.videos = self.streams.filter(subtype='mp4',
                                          is_dash=True
                                          ).order_by('resolution'
                                          ).desc()

        self.audios = self.streams.filter(type='audio',
                                          mime_type='audio/webm',
                                          audio_codec='opus',
                                          ).order_by('abr').desc()

        self._streams = {'videos': self.videos,
                         'audios': self.audios}

        self.path = path

        self._video_path = ''
        self._audio_path = ''

        self._title = self.title.replace(' ', '_')
        
        self.window = window


    def download_video(self,
                       res: str = '',
                       fps: int = 0) -> None:
        """
        Download a video, its audio and merge them
        to the best possible quality mp4.
        
        Parameters
        ----------
        res : `str`
            Video resolution as string (i.e. '720p').
            
        fps : `int`
            Video framerate.
            
        Notes
        -----
        If res or fps are not supplied, the method will
        download the video on the best quality possible.
        """
        if res and fps:
            video = self.videos.filter(res=res,
                                       fps=fps).first()
        else:
            # Taking the best possible resolution for the video,
            # since get_by_resolution method just work on progressive
            # streams (720p max) only.
            video = None

            for r in RESOLUTIONS:
                for v in self.videos:

                    if v.resolution == r:
                        video = v
                        break

                    if video:
                        break

        self.window.s_append(f'Downloading now video for {self.title}')

        # Stores video and audio path and merge them
        self._video_path = video.download(output_path=self.path,
                                          filename='video')

        self._audio_path = self.download_audio()

        self.merge()

    def download_audio(self,
                       bitrate: str = '',
                       title:   bool = False) -> Union[str, None]:
        """
        Downloads audio only for a video
        
        Parameters
        ----------
        bitrate : `str`
            String containing an audio bitrate 
            to download (e.g '128kbps).
            
        title : `bool`
            If True, the video will be downloaded
            with it's original title.
        
        Notes
        -----
        Returns the downloaded audio path if bitrate was supplied.
        """
        fn = 'audio' if not title else self._title

        self.window.s_append(f'Downloading now audio for {self.title}')

        if not bitrate and not title:
            path = Path(self.audios.get_audio_only(subtype='webm'
                                                   ).download(output_path=self.path,
                                                              filename=fn))

            return str(path.rename(path.with_suffix('.mp3')))
            
        else:
            audio = self.audios.filter(abr=bitrate).first()

            path = Path(audio.download(output_path=self.path,
                                       filename=self._title))

            path.rename(path.with_suffix('.mp3'))

    def merge(self) -> None:
        """
        Merge no-sound video and audio files into an mp4.
        
        Notes
        -----
        This method requires ffmpeg installed to work.
        
        If self.path is not supplied, it will merge the files
        into the current working directory.
        """
        
        if not self.path:
            self.path = os.getcwd()
        
        self.window.s_append(f'Merging video and audio for {self.title}')

        ffmpeg = subprocess.Popen(FFMPEG_CMD.format(self).split(' '),
                                  stdout=subprocess.DEVNULL)

        while not ffmpeg.poll():
            # Await until process is complete
            # before deleting input files
            if ffmpeg.poll() == 0:
                break
            time.sleep(0.5)

        os.remove(self._audio_path)
        os.remove(self._video_path)

    def __len__(self):
        return len([s for i in self._streams for s in i])-1

    def __getitem__(self, key: str) -> List[pytube.StreamQuery]:
        return self._streams[key]


class Playlist(pytube.Playlist):
    """
    Playlist class that inherits pytube.Playlist
    It fixes a pytube Playlist regex error and appends
    window to status some details about the searched playlist.
    
    Parameters
    ----------
    url : `str`
        Searched playlist url
        
    window : `Window`
        Window object used for status updating
    """
    def __init__(self,
                 url: str,
                 window: Window) -> None:

        super().__init__(url=url)

        # Fixing pytube Playlist regex error
        self._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        
        window.update_header(f'\nTitle: {self.title()}',
                             f'Tracks: {self.__len__()}')
