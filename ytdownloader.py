#!/usr/bin/env python3

# Coded By f4ll_py #
try:
    import PySimpleGUI as sg
    from pytube import YouTube, Playlist
    from re import compile
    from subprocess import call
    from os import path, remove, rename
    from time import sleep
    from urllib import error
    from sys import platform
except Exception as e:
    print(f'An error has occurred with a module: {e}')
else:
    def ytdownloader():
        sg.theme('SystemDefault1')
        frame_layout = [
            [sg.Text('       URL', justification = 'left', font = 'Calibri'), sg.InputText(size = (85, 0), key = 'url', font = 'Calibri'), sg.Button('     GO    ', button_color = ('Black', 'White'), font = 'Calibri')],
            [sg.Text('  Output', justification = 'left', font = 'Calibri'), sg.InputText(size = (85, 0), key = 'path', disabled = True, font = 'Calibri'), sg.FolderBrowse('BROWSE', button_color = ('Black', 'White'), font = 'Calibri')],
            [sg.Text('')],
            [sg.Text('Title: ', font = 'Calibri', size = (90, 0), key = 'title')],
            [sg.Text('Author: ', font = 'Calibri', size = (90,0), key = 'author')],
            [sg.Text('Length: ', font = 'Calibri', size = (90, 0), key = 'length')],
            [sg.Text('')],
            [sg.Text('Output:', font = 'Calibri')],
            [sg.Multiline(font = 'Calibri', key = 'return', size = (100, 15), disabled = True, border_width = '0')],
            [sg.Text(' Stream', font = 'Calibri', justification = 'left'), sg.Combo(values = '', size = (20, 0), key = 'output', readonly = True, font = 'Calibri'), sg.Button('Download', font = 'Calibri')]
        ]

        layout = [
            [sg.Frame('', frame_layout)]
        ]

        window = sg.Window('YTDownloader 0.4', layout, icon = r'icon.ico')
        while True:
            event, values = window.read()
            path_file = values['path']
            if event == sg.WINDOW_CLOSED:
                break
            if event == '     GO    ':
                try:
                    yt = YouTube(values['url'])
                    window['title'].update(f'Title: {yt.title}')
                    window['author'].update(f'Author: {yt.author}', visible = True)
                    window['length'].update(f'Length: {yt.length/60:.0f} minutes', visible = True)
                    #60FPS
                    if yt.streams.get_by_itag('315') and yt.streams.get_by_itag('308') and yt.streams.get_by_itag('299') and yt.streams.get_by_itag('298') in yt.streams:
                        window['output'].update(values = ['_______60FPS_______', '2160p60', '1440p60', '1080p60', '720p60', '_______30FPS_______','2160p','1440p','1080p', '720p', '480p', '360p', '240p', '144p', '_______AUDIO_______', '160kbps', '128kbps'])
                        window['return'].update('')
                        window['return'].update('''60FPS
        2160p60
        1440p60
        1080p60
        720p60
30FPS
        2160p
        1440p
        1080p
        720p
        480p
        360p
        240p
        144p
AUDIO
        160kbps
        128kbps''')
                    elif yt.streams.get_by_itag('308') and yt.streams.get_by_itag('299') and yt.streams.get_by_itag('298') in yt.streams:
                        window['output'].update(values = ['_______60FPS_______', '1440p60', '1080p60', '720p60', '_______30FPS_______','1440p','1080p', '720p', '480p', '360p', '240p', '144p', '_______AUDIO_______', '160kbps', '128kbps'])
                        window['return'].update('')
                        window['return'].update('''60FPS
        1440p60
        1080p60
        720p60
30FPS
        1440p
        1080p
        720p
        480p
        360p
        240p
        144p
AUDIO
        160kbps
        128kbps''')
                    elif yt.streams.get_by_itag('299') and yt.streams.get_by_itag('298') in yt.streams:
                            window['output'].update(values = ['_______60FPS_______', '1080p60', '720p60', '_______30FPS_______','1080p', '720p', '480p', '360p', '240p', '144p', '_______AUDIO_______', '160kbps', '128kbps'])
                            window['return'].update('')
                            window['return'].update('''60FPS
        1080p60
        720p60
30FPS
        1080p
        720p
        480p
        360p
        240p
        144p
AUDIO
        160kbps
        128kbps''')
                    elif yt.streams.get_by_itag('298') in yt.streams:
                            window['output'].update(values = ['_______60FPS_______', '720p60', '_______30FPS_______', '720p', '480p', '360p', '240p', '144p', '_______AUDIO_______', '160kbps', '128kbps'])
                            window['return'].update('')
                            window['return'].update('''60FPS
        720p60
30FPS
        720p
        480p
        360p
        240p
        144p
AUDIO
        160kbps
        128kbps''')
                #30FPS
                    elif yt.streams.get_by_itag('313') and yt.streams.get_by_itag('271') and yt.streams.get_by_itag('137') and yt.streams.get_by_itag('136') and yt.streams.get_by_itag('135') and yt.streams.get_by_itag('134') and yt.streams.get_by_itag('133') and yt.streams.get_by_itag('160') in yt.streams:
                        window['output'].update(values = ['_______30FPS_______', '2160p', '1440p', '1080p', '720p', '480p', '360p', '240p', '144p', '_______AUDIO_______', '160kbps', '128kbps'])
                        window['return'].update('')
                        window['return'].update('''30FPS
        2160p
        1440p
        1080p
        720p
        480p
        360p
        240p
        144p
AUDIO
        160kbps
        128kbps''')
                    elif yt.streams.get_by_itag('271') and yt.streams.get_by_itag('137') and yt.streams.get_by_itag('136') and yt.streams.get_by_itag('135') and yt.streams.get_by_itag('134') and yt.streams.get_by_itag('133') and yt.streams.get_by_itag('160') in yt.streams:
                        window['output'].update(values = ['_______30FPS_______', '1440p', '1080p', '720p', '480p', '360p', '240p', '144p', '_______AUDIO_______', '160kbps', '128kbps'])
                        window['return'].update('')
                        window['return'].update('''30FPS
        1440p
        1080p
        720p
        480p
        360p
        240p
        144p
AUDIO
        160kbps
        128kbps''')
                    elif yt.streams.get_by_itag('137') and yt.streams.get_by_itag('136') and yt.streams.get_by_itag('135') and yt.streams.get_by_itag('134') and yt.streams.get_by_itag('133') and yt.streams.get_by_itag('160') in yt.streams:
                        window['output'].update(values = ['_______30FPS_______', '1080p', '720p', '480p', '360p', '240p', '144p', '_______AUDIO_______', '160kbps', '128kbps'])
                        window['return'].update('')
                        window['return'].update('''30FPS
        1080p
        720p
        480p
        360p
        240p
        144p
AUDIO
        160kbps
        128kbps''')
                    elif yt.streams.get_by_itag('136') and yt.streams.get_by_itag('135') and yt.streams.get_by_itag('134') and yt.streams.get_by_itag('133') and yt.streams.get_by_itag('160') in yt.streams:
                        window['output'].update(values = ['_______30FPS_______', '720p', '480p', '360p', '240p', '144p', '_______AUDIO_______', '160kbps', '128kbps'])
                        window['return'].update('')
                        window['return'].update('''30FPS
        720p
        480p
        360p
        240p
        144p
AUDIO
        160kbps
        128kbps''')
                    elif yt.streams.get_by_itag('135') and yt.streams.get_by_itag('134') and yt.streams.get_by_itag('133') and yt.streams.get_by_itag('160') in yt.streams:
                        window['output'].update(values = ['_______30FPS_______', '480p', '360p', '240p', '144p', '_______AUDIO_______', '160kbps', '128kbps'])
                        window['return'].update('')
                        window['return'].update('''30FPS
        480p
        360p
        240p
        144p
AUDIO
        160kbps
        128kbps''')
                    elif yt.streams.get_by_itag('134') and yt.streams.get_by_itag('133') and yt.streams.get_by_itag('160') in yt.streams:
                        window['output'].update(values = ['_______30FPS_______', '360p', '240p', '144p', '_______AUDIO_______', '160kbps', '128kbps'])
                        window['return'].update('')
                        window['return'].update('''30FPS
        360p
        240p
        144p
AUDIO
        160kbps
        128kbps''')
                    elif yt.streams.get_by_itag('133') and yt.streams.get_by_itag('160') in yt.streams:
                        window['output'].update(values = ['_______30FPS_______', '240p', '144p', '_______AUDIO_______', '160kbps', '128kbps'])
                        window['return'].update('')
                        window['return'].update('''30FPS
        240p
        144p
AUDIO
        160kbps
        128kbps''')
                    elif yt.streams.get_by_itag('160') in yt.streams:
                        window['output'].update(values = ['_______30FPS_______', '144p', '_______AUDIO_______', '160kbps', '128kbps'])
                        window['return'].update('')
                        window['return'].update('''30FPS
        144p
AUDIO
        160kbps
        128kbps''')
                except KeyError:
                    window['return'].update('An error with the cipher has ocurred. See documentation in Github to resolve.')
                except:
                    i = 1
                    pl = Playlist(values['url'])
                    pl._video_regex = compile(r"\"url\":\"(/watch\?v=[\w-]*)")
                    window['title'].update(f'Videos in current playlist: {len(pl.video_urls)}')
                    window['author'].update(visible = False)
                    window['length'].update(visible = False)
                    window['output'].update(values = ['Video (Progressive)', 'Audio (128kbps)'])
                    window['return'].update('')
                    window['return'].update('''VIDEO
        The best quality until 720p
AUDIO
        128kbps''')
            #DOWNLOAD - VIDEO
            if event == 'Download':
                try:
                    combo = values['output']
                    print(combo)
                    try:
                        if combo == '2160p60':
                            extension = 'mp4'
                            window['return'].update(f'Downloading {yt.title}... Please Wait.')
                            window.Refresh()
                            YouTube(values['url']).streams.get_by_itag('315').download(filename = 'video')
                            YouTube(values['url']).streams.get_by_itag('251').download(filename = 'audio')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.')
                            window.Refresh()
                            call(["ffmpeg", "-i",
                            path.join('video.webm'),
                            "-i", 
                            path.join('audio.webm'),
                            path.join(f'{yt.title}.mp4')
                            ])
                            sleep(0.5)
                            remove('video.webm')
                            remove('audio.webm')
                            sleep(0.5)
                            if platform == 'win32' or platform == 'win64':
                                if path_file != '':
                                    rename(f'{yt.title}.mp4', f'{path_file}\\{yt.title}.mp4')
                            elif platform == 'linux':
                                if path_file != '':
                                    rename(f'{yt.title}.mp4', f'{path_file}/{yt.title}.mp4')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.\n\nMerging completed, downloaded files has moved to output path.')
                        elif combo == '1440p60':
                            extension = 'mp4'
                            window['return'].update(f'Downloading {yt.title}... Please Wait.')
                            window.Refresh()
                            YouTube(values['url']).streams.get_by_itag('308').download(filename = 'video')
                            YouTube(values['url']).streams.get_by_itag('251').download(filename = 'audio')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.')
                            window.Refresh()
                            call(["ffmpeg", "-i",
                            path.join('video.webm'),
                            "-i", 
                            path.join('audio.webm'),
                            path.join(f'{yt.title}.mp4')
                            ])
                            sleep(0.5)
                            remove('video.webm')
                            remove('audio.webm')
                            sleep(0.5)
                            if platform == 'win32' or platform == 'win64':
                                if path_file != '':
                                    rename(f'{yt.title}.mp4', f'{path_file}\\{yt.title}.mp4')
                            elif platform == 'linux':
                                if path_file != '':
                                    rename(f'{yt.title}.mp4', f'{path_file}/{yt.title}.mp4')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.\n\nMerging completed, downloaded files has moved to output path.')
                        elif combo == '1080p60':
                            extension = 'mp4'
                            window['return'].update(f'Downloading {yt.title}... Please Wait.')
                            window.Refresh()
                            YouTube(values['url']).streams.get_by_itag('299').download(filename = 'video')
                            YouTube(values['url']).streams.get_by_itag('140').download(filename = 'audio')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.')
                            window.Refresh()
                            call(["ffmpeg", "-i",
                            path.join('video.mp4'),
                            "-i", 
                            path.join('audio.mp4'),
                            path.join(f'{yt.title}.mp4')
                            ])
                            sleep(0.5)
                            remove('video.mp4')
                            remove('audio.mp4')
                            sleep(0.5)
                            if platform == 'win32' or platform == 'win64':
                                if path_file != '':
                                    rename(f'{yt.title}.mp4', f'{path_file}\\{yt.title}.mp4')
                            elif platform == 'linux':
                                if path_file != '':
                                    rename(f'{yt.title}.mp4', f'{path_file}/{yt.title}.mp4')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.\n\nMerging completed, downloaded files has moved to output path.')
                        elif combo == '720p60':
                            extension = 'mp4'
                            window['return'].update(f'Downloading {yt.title}... Please Wait.')
                            window.Refresh()
                            YouTube(values['url']).streams.get_by_itag('298').download(filename = 'video')
                            YouTube(values['url']).streams.get_by_itag('140').download(filename = 'audio')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.')
                            window.Refresh()
                            call(["ffmpeg", "-i",
                            path.join('video.mp4'),
                            "-i", 
                            path.join('audio.mp4'),
                            path.join(f'{yt.title}.mp4')
                            ])
                            sleep(0.5)
                            remove('video.mp4')
                            remove('audio.mp4')
                            sleep(0.5)
                            if platform == 'win32' or platform == 'win64':
                                if path_file != '':
                                    rename(f'{yt.title}.mp4', f'{path_file}\\{yt.title}.mp4')
                            elif platform == 'linux':
                                if path_file != '':
                                    rename(f'{yt.title}.mp4', f'{path_file}/{yt.title}.mp4')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.\n\nMerging completed, downloaded files has moved to output path.')
                        elif combo == '2160p':
                            extension = 'mp4'
                            window['return'].update(f'Downloading {yt.title}... Please Wait.')
                            window.Refresh()
                            YouTube(values['url']).streams.get_by_itag('313').download(filename = 'video')
                            YouTube(values['url']).streams.get_by_itag('251').download(filename = 'audio')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.')
                            window.Refresh()
                            call(["ffmpeg", "-i",
                            path.join('video.webm'),
                            "-i", 
                            path.join('audio.webm'),
                            path.join(f'{yt.title}.mp4')
                            ])
                            sleep(0.5)
                            remove('video.webm')
                            remove('audio.webm')
                            sleep(0.5)
                            if platform == 'win32' or platform == 'win64':
                                if path_file != '':
                                    rename(f'{yt.title}.mp4', f'{path_file}\\{yt.title}.mp4')
                            elif platform == 'linux':
                                if path_file != '':
                                    rename(f'{yt.title}.mp4', f'{path_file}/{yt.title}.mp4')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.\n\nMerging completed, downloaded files has moved to output path.')
                        elif combo == '1440p':
                            extension = 'mp4'
                            window['return'].update(f'Downloading {yt.title}... Please Wait.')
                            window.Refresh()
                            YouTube(values['url']).streams.get_by_itag('271').download(filename = 'video')
                            YouTube(values['url']).streams.get_by_itag('251').download(filename = 'audio')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.')
                            window.Refresh()
                            call(["ffmpeg", "-i",
                            path.join('video.webm'),
                            "-i", 
                            path.join('audio.webm'),
                            path.join(f'{yt.title}.mp4')
                            ])
                            sleep(0.5)
                            remove('video.webm')
                            remove('audio.webm')
                            sleep(0.5)
                            if platform == 'win32' or platform == 'win64':
                                if path_file != '':
                                    rename(f'{yt.title}.mp4', f'{path_file}\\{yt.title}.mp4')
                            elif platform == 'linux':
                                if path_file != '':
                                    rename(f'{yt.title}.mp4', f'{path_file}/{yt.title}.mp4')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.\n\nMerging completed, downloaded files has moved to output path.')
                        elif combo == '1080p':
                            extension = 'mp4'
                            window['return'].update(f'Downloading {yt.title}... Please Wait.')
                            window.Refresh()
                            YouTube(values['url']).streams.get_by_itag('137').download(filename = 'video')
                            YouTube(values['url']).streams.get_by_itag('140').download(filename = 'audio')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.')
                            window.Refresh()
                            call(["ffmpeg", "-i",
                            path.join('video.mp4'),
                            "-i", 
                            path.join('audio.mp4'),
                            path.join(f'{yt.title}.mp4')
                            ])
                            sleep(0.5)
                            remove('video.mp4')
                            remove('audio.mp4')
                            sleep(0.5)
                            if platform == 'win32' or platform == 'win64':
                                if path_file != '':
                                    rename(f'{yt.title}.mp4', f'{path_file}\\{yt.title}.mp4')
                            elif platform == 'linux':
                                if path_file != '':
                                    rename(f'{yt.title}.mp4', f'{path_file}/{yt.title}.mp4')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.\n\nMerging completed, downloaded files has moved to output path.')
                        elif combo == '720p':
                            extension = 'mp4'
                            if yt.streams.get_by_itag('22') in yt.streams:
                                window['return'].update(f'Downloading {yt.title}... Please Wait.')
                                window.Refresh()
                                YouTube(values['url']).streams.get_by_itag('22').download()
                                window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.')
                                if platform == 'win32' or platform == 'win64':
                                    if path_file != '':
                                        rename(f'{yt.title}.mp4', f'{path_file}\\{yt.title}.mp4')
                                elif platform == 'linux':
                                    if path_file != '':
                                        rename(f'{yt.title}.mp4', f'{path_file}/{yt.title}.mp4')
                                window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nDownloaded files has moved to output path.')
                            else:
                                extension = 'mp4'
                                window['return'].update(f'Downloading {yt.title}... Please Wait.')
                                window.Refresh()
                                YouTube(values['url']).streams.get_by_itag('136').download(filename = 'video')
                                YouTube(values['url']).streams.get_by_itag('140').download(filename = 'audio')
                                window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.')
                                window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.')
                                window.Refresh()
                                call(["ffmpeg", "-i",
                                path.join('video.mp4'),
                                "-i", 
                                path.join('audio.mp4'),
                                path.join(f'{yt.title}.mp4')
                                ])
                                sleep(0.5)
                                remove('video.mp4')
                                remove('audio.mp4')
                                sleep(0.5)
                                if platform == 'win32' or platform == 'win64':
                                    if path_file != '':
                                        rename(f'{yt.title}.mp4', f'{path_file}\\{yt.title}.mp4')
                                elif platform == 'linux':
                                    if path_file != '':
                                        rename(f'{yt.title}.mp4', f'{path_file}/{yt.title}.mp4')
                                window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.\n\nMerging completed, downloaded files has moved to output path.')
                        elif combo == '480p':
                            extension = 'mp4'
                            window['return'].update(f'Downloading {yt.title}... Please Wait.')
                            window.Refresh()
                            YouTube(values['url']).streams.get_by_itag('135').download(filename = 'video')
                            YouTube(values['url']).streams.get_by_itag('140').download(filename = 'audio')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.')
                            window.Refresh()
                            call(["ffmpeg", "-i",
                            path.join('video.mp4'),
                            "-i", 
                            path.join('audio.mp4'),
                            path.join(f'{yt.title}.mp4')
                            ])
                            sleep(0.5)
                            remove('video.mp4')
                            remove('audio.mp4')
                            sleep(0.5)
                            if platform == 'win32' or platform == 'win64':
                                if path_file != '':
                                    rename(f'{yt.title}.mp4', f'{path_file}\\{yt.title}.mp4')
                            elif platform == 'linux':
                                if path_file != '':
                                    rename(f'{yt.title}.mp4', f'{path_file}/{yt.title}.mp4')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.\n\nMerging completed, downloaded files has moved to output path.')
                        elif combo == '360p':
                            extension = 'mp4'
                            if yt.streams.get_by_itag('18') in yt.streams:
                                window['return'].update(f'Downloading {yt.title}... Please Wait.')
                                window.Refresh()
                                YouTube(values['url']).streams.get_by_itag('18').download()
                                window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.')
                                if path_file != '':
                                    rename(f'{yt.title}.mp4', f'{path_file}\\{yt.title}.mp4')
                                window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nDownloaded files has moved to output path.')
                            else:
                                window['return'].update(f'Downloading {yt.title}... Please Wait.')
                                window.Refresh()
                                YouTube(values['url']).streams.get_by_itag('134').download(filename = 'video')
                                YouTube(values['url']).streams.get_by_itag('140').download(filename = 'audio')
                                window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.')
                                window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.')
                                window.Refresh()
                                call(["ffmpeg", "-i",
                                path.join('video.mp4'),
                                "-i", 
                                path.join('audio.mp4'),
                                path.join(f'{yt.title}.mp4')
                                ])
                                sleep(0.5)
                                remove('video.mp4')
                                remove('audio.mp4')
                                sleep(0.5)
                                if platform == 'win32' or platform == 'win64':
                                    if path_file != '':
                                        rename(f'{yt.title}.mp4', f'{path_file}\\{yt.title}.mp4')
                                elif platform == 'linux':
                                    if path_file != '':
                                        rename(f'{yt.title}.mp4', f'{path_file}/{yt.title}.mp4')
                                window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.\n\nMerging completed, downloaded files has moved to output path.')
                        elif combo == '240p':
                            extension = 'mp4'
                            window['return'].update(f'Downloading {yt.title}... Please Wait.')
                            window.Refresh()
                            YouTube(values['url']).streams.get_by_itag('133').download(filename = 'video')
                            YouTube(values['url']).streams.get_by_itag('140').download(filename = 'audio')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.')
                            window.Refresh()
                            call(["ffmpeg", "-i",
                            path.join('video.mp4'),
                            "-i", 
                            path.join('audio.mp4'),
                            path.join(f'{yt.title}.mp4')
                            ])
                            sleep(0.5)
                            remove('video.mp4')
                            remove('audio.mp4')
                            sleep(0.5)
                            if platform == 'win32' or platform == 'win64':
                                if path_file != '':
                                    rename(f'{yt.title}.mp4', f'{path_file}\\{yt.title}.mp4')
                            elif platform == 'linux':
                                if path_file != '':
                                    rename(f'{yt.title}.mp4', f'{path_file}/{yt.title}.mp4')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.\n\nMerging completed, downloaded files has moved to output path.')
                        elif combo == '144p':
                            extension = 'mp4'
                            window['return'].update(f'Downloading {yt.title}... Please Wait.')
                            window.Refresh()
                            YouTube(values['url']).streams.get_by_itag('160').download(filename = 'video')
                            YouTube(values['url']).streams.get_by_itag('140').download(filename = 'audio')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.')
                            window.Refresh()
                            call(["ffmpeg", "-i",
                            path.join('video.mp4'),
                            "-i", 
                            path.join('audio.mp4'),
                            path.join(f'{yt.title}.mp4')
                            ])
                            sleep(0.5)
                            remove('video.mp4')
                            remove('audio.mp4')
                            sleep(0.5)
                            if platform == 'win32' or platform == 'win64':
                                if path_file != '':
                                    rename(f'{yt.title}.mp4', f'{path_file}\\{yt.title}.mp4')
                            elif platform == 'linux':
                                if path_file != '':
                                    rename(f'{yt.title}.mp4', f'{path_file}/{yt.title}.mp4')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nMerging... Check terminal to follow the process.\n\nMerging completed, downloaded files has moved to output path.')
                        elif combo == 'Video (Progressive)':
                            extension = 'mp4p'
                            for video in pl.video_urls:
                                window['return'].update(f'Downloading {YouTube(video).title}... Please Wait.')
                                window.Refresh()
                                YouTube(video).streams.get_highest_resolution().download()
                                if i == 0:
                                    window['return'].update(f'Downloading {YouTube(video).title}... Please Wait.\n\n{i} Download Completed.')
                                else:
                                    window['return'].update(f'Downloading {YouTube(video).title}... Please Wait.\n\n{i} Downloads Completed.')
                                if platform == 'win32' or platform == 'win64':
                                    if path_file != '':
                                        rename(f'{YouTube(video).title}.mp4', f'{path_file}\\{YouTube(video).title}.mp4')
                                elif platform == 'linux':
                                    if path_file != '':
                                        rename(f'{YouTube(video).title}.mp4', f'{path_file}/{YouTube(video).title}.mp4')
                                if i == len(pl.video_urls):
                                    window['return'].update(f'Downloading {YouTube(video).title}... Please Wait.\n\n{i} Downloads Completed.\n\nDownloaded files has moved to output path.')
                                i += 1
                    except KeyError:
                        window['return'].update('An error with the cipher has ocurred. See documentation in Github to resolve.')
                    except FileExistsError:
                        window['return'].update('Another file with same name already exists.')
                        if extension == 'mp4':
                            remove(f'{yt.title}.mp4')
                        elif extension == 'mp4p':
                            remove(f'{YouTube(video).title}.mp4')
                    #AUDIO
                    try:
                        if combo == '128kbps':
                            extension = 'mp3'
                            window['return'].update(f'Downloading {yt.title}... Please Wait.')
                            window.Refresh()
                            YouTube(values['url']).streams.get_by_itag('140').download(filename = 'audio')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nConverting... Check terminal to follow the process.')
                            window.Refresh()
                            call(["ffmpeg", "-i",
                            path.join('audio.mp4'),
                            path.join(f'{yt.title}.mp3')
                            ])
                            sleep(0.5)
                            remove('audio.mp4')
                            sleep(0.5)
                            if platform == 'win32' or platform == 'win64':
                                if path_file != '':
                                    rename(f'{yt.title}.mp3', f'{path_file}\\{yt.title}.mp3')
                            elif platform == 'linux':
                                if path_file != '':
                                    rename(f'{yt.title}.mp3', f'{path_file}/{yt.title}.mp3')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nConverting... Check terminal to follow the process.\n\nConverting completed, downloaded files has moved to output path.')
                        elif combo == '160kbps':
                            extension = 'mp3'
                            window['return'].update(f'Downloading {yt.title}... Please Wait.')
                            window.Refresh()
                            YouTube(values['url']).streams.get_by_itag('251').download(filename = 'audio')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nConverting... Check terminal to follow the process.')
                            window.Refresh()
                            call(["ffmpeg", "-i",
                            path.join('audio.webm'),
                            path.join(f'{yt.title}.mp3')
                            ])
                            sleep(0.5)
                            remove('audio.webm')
                            sleep(0.5)
                            if platform == 'win32' or platform == 'win64':
                                if path_file != '':
                                    rename(f'{yt.title}.mp3', f'{path_file}\\{yt.title}.mp3')
                            elif platform == 'linux':
                                if path_file != '':
                                    rename(f'{yt.title}.mp3', f'{path_file}/{yt.title}.mp3')
                            window['return'].update(f'Downloading {yt.title}... Please Wait.\n\nDownload Completed.\n\nConverting... Check terminal to follow the process.\n\nConverting completed, downloaded files has moved to output path.')
                        elif combo == 'Audio (128kbps)':
                            extension = 'mp3p'
                            for music in pl.video_urls:
                                window['return'].update(f'Downloading {YouTube(music).title}... Please Wait.')
                                window.Refresh()
                                YouTube(music).streams.get_by_itag('140').download(filename = f'music{i}')
                                if i == 0:
                                    window['return'].update(f'Downloading {YouTube(music).title}... Please Wait.\n\n{i} Download Completed.')
                                else:
                                    window['return'].update(f'Downloading {YouTube(music).title}... Please Wait.\n\n{i} Downloads Completed.')
                                window['return'].update(f'Downloading {YouTube(music).title}... Please Wait.\n\n{i} Downloads Completed.\n\nStarting conversion... Check terminal to follow the process.')
                                window.Refresh()
                                call(["ffmpeg", "-i",
                                path.join(f'music{i}.mp4'),
                                path.join(f'music{i}.mp3')
                                ])
                                remove(f'music{i}.mp4')
                                sleep(0.5)
                                rename(f'music{i}.mp3', f'{YouTube(music).title}.mp3')
                                sleep(0.5)
                                if platform == 'win32' or platform == 'win64':
                                    if path_file != '':
                                        rename(f'{YouTube(video).title}.mp3', f'{path_file}\\{YouTube(video).title}.mp3')
                                elif platform == 'linux':
                                    if path_file != '':
                                        rename(f'{YouTube(video).title}.mp3', f'{path_file}/{YouTube(video).title}.mp3')
                                if i == len(pl.video_urls):
                                    window['return'].update(f'Downloading {YouTube(music).title}... Please Wait.\n\n{i} Downloads Completed.\n\nConverting completed, downloaded files has moved to output path.')
                                i +=1
                    except KeyError:
                        window['return'].update('An error with the cipher has ocurred. See documentation in Github to resolve.')
                    except FileExistsError:
                        window['return'].update('Another file with same name already exists.')
                        if extension == 'mp3':
                            remove(f'{yt.title}.mp3')
                        elif extension == 'mp3p':
                            remove(f'{YouTube(music).title}.mp3')
                except KeyError:
                    window['return'].update('An error with the cipher has ocurred. See documentation in Github to resolve.')
                except error.HTTPError:
                    window['return'].update('This file is unavailable. Try another.')
        window.close()

    class main:
        ytdownloader()