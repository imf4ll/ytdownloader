#!/usr/bin/env python3
try:
    from pytube import YouTube, Playlist
    from subprocess import call
    from os import path, remove, rename
    from time import sleep
    from re import compile
    from getpass import getuser
    from sys import platform
    from urllib import error
except Exception as e:
    print()
    print(f'\033[31mError with a module: {e}\033[m')
    print("\033[31mTry 'pip install -r dependencies.txt' to install all modules.\033[m")
    print()
else:
    def yt(url):
        i = 1
        while True:
            opt_type = int(input('\n\n\033[33m[ 0 ] Cancel\n\033[33m[ 1 ] \033[34mVideo\n\033[33m[ 2 ] \033[34mPlaylist\n> \033[m'))
            if opt_type == 1:
                while True:
                    try:
                        ytb = YouTube(url)
                        ytb._video_regex = compile(r"\"url\":\"(/watch\?v=[\w-]*)")
                        print(f'\n\033[33mTitle: \033[34m{ytb.title}\033[m')
                        print(f'\033[33mAuthor: \033[34m{ytb.author}\033[m')
                        print(f'\033[33mLength: \033[34m{ytb.length/60:.0f} minutes.\033[m')
                        print('\033[33m='*50,'\n')
                        if ytb.streams.get_by_itag('299') or ytb.streams.get_by_itag('298') or ytb.streams.get_by_itag('308') or ytb.streams.get_by_itag('315') in ytb.streams:
                            opt_format60 = int(input('\033[33m[ 0 ] Cancel\n\033[33m[ 1 ] \033[34mVideo \033[33m(60 FPS)\n\033[33m[ 2 ] \033[34mVideo \033[33m(30 FPS)\n\033[33m[ 3 ] \033[34mAudio \033[33m(128 Kbps)\033[34m\n> \033[m'))
                            print('\033[33m='*50,'\n')
                            if opt_format60 == 1:
                                while True:
                                    try:
                                        if ytb.streams.get_by_itag('315') and ytb.streams.get_by_itag('308') and ytb.streams.get_by_itag('299') and ytb.streams.get_by_itag('298') in ytb.streams:
                                            opt_download = int(input('\033[33m[ 0 ] \033[33mCancel\n\033[33m[ 1 ] \033[34m2160p60\n\033[33m[ 2 ] \033[34m1440p60\n\033[33m[ 3 ] \033[34m1080p60\n\033[33m[ 4 ] \033[34m720p60\n> \033[m'))
                                            if opt_download > 4 or opt_download < 0:
                                                print('\n\033[31m> Invalid option.\033[m\n')
                                                continue
                                            if opt_download == 0:
                                                break
                                            print(f'\n\033[34m> Downloading \033[31m{ytb.title}\033[34m... \033[33mPlease, wait.\033[m')
                                            if opt_download == 1:
                                                YouTube(url).streams.get_by_itag('315').download(filename='video')
                                                YouTube(url).streams.get_by_itag('251').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.webm'),
                                                "-i", 
                                                path.join('audio.webm'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.webm')
                                                remove('audio.webm')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 2:
                                                YouTube(url).streams.get_by_itag('308').download(filename='video')
                                                YouTube(url).streams.get_by_itag('251').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.webm'),
                                                "-i", 
                                                path.join('audio.webm'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.webm')
                                                remove('audio.webm')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 3:
                                                YouTube(url).streams.get_by_itag('299').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 4:
                                                YouTube(url).streams.get_by_itag('298').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                        elif ytb.streams.get_by_itag('308') and ytb.streams.get_by_itag('299') and ytb.streams.get_by_itag('298') in ytb.streams:
                                            opt_download = int(input('\033[33m[ 0 ] \033[33mCancel\n\033[33m[ 1 ] \033[34m1440p60\n\033[33m[ 2 ] \033[34m1080p60\n\033[33m[ 3 ] \033[34m720p60\n> \033[m'))
                                            if opt_download > 3 or opt_download < 0:
                                                print('\n\033[31m> Invalid option.\033[m\n')
                                                continue
                                            if opt_download == 0:
                                                break
                                            print(f'\n\033[34m> Downloading \033[31m{ytb.title}\033[34m... \033[33mPlease, wait.\033[m')
                                            if opt_download == 1:
                                                YouTube(url).streams.get_by_itag('308').download(filename='video')
                                                YouTube(url).streams.get_by_itag('251').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.webm'),
                                                "-i", 
                                                path.join('audio.webm'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.webm')
                                                remove('audio.webm')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 2:
                                                YouTube(url).streams.get_by_itag('299').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 3:
                                                YouTube(url).streams.get_by_itag('298').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                        elif ytb.streams.get_by_itag('299') and ytb.streams.get_by_itag('298')  in ytb.streams:
                                            opt_download = int(input('\033[33m[ 0 ] \033[33mCancel\n\033[33m[ 1 ] \033[34m1080p60\n\033[33m[ 2 ] \033[34m720p60\n> \033[m'))
                                            if opt_download > 2 or opt_download < 0:
                                                print('\n\033[31m> Invalid option.\033[m\n')
                                                continue
                                            if opt_download == 0:
                                                break
                                            print(f'\n\033[34m> Downloading \033[31m{ytb.title}\033[34m... \033[33mPlease, wait.\033[m')
                                            if opt_download == 1:
                                                YouTube(url).streams.get_by_itag('299').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 2:
                                                YouTube(url).streams.get_by_itag('298').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                        elif ytb.streams.get_by_itag('298') in ytb.streams:
                                            opt_download = int(input('\033[33m[ 0 ] \033[33mCancel\n\033[33m[ 1 ] \033[34m720p60\n\033[34m> \033[m'))
                                            if opt_download > 1 or opt_download < 0:
                                                print('\n\033[31m> Invalid option.\033[m\n')
                                                continue
                                            if opt_download == 0:
                                                break
                                            print(f'\n\033[34m> Downloading \033[31m{ytb.title}\033[34m... \033[33mPlease, wait.\033[m')
                                            if opt_download == 1:
                                                YouTube(url).streams.get_by_itag('298').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                        break
                                    except error.HTTPError:
                                        print('\n\033[31m> This file is unavailable for download, please choose another.\033[m\n')
                                        continue
                                    except FileExistsError:
                                        print('\n\033[31m> The file already exists.\033[m')
                                        remove(f'{ytb.title}.mp4')
                                        break   
                                    except:
                                        print('\n\033[31m> An unknown error has occurred.\033[m\n')
                                        break
                            elif opt_format60 == 2:
                                while True:
                                        try:
                                            if ytb.streams.get_by_itag('313') and ytb.streams.get_by_itag('271') and ytb.streams.get_by_itag('137') and ytb.streams.get_by_itag('136') and ytb.streams.get_by_itag('135') and ytb.streams.get_by_itag('134') and ytb.streams.get_by_itag('133') and ytb.streams.get_by_itag('160') in ytb.streams:
                                                opt_download = int(input('\033[33m[ 0 ] \033[33mCancel\n\033[33m[ 1 ] \033[34m2160p\n\033[33m[ 2 ] \033[34m1440p\n\033[33m[ 3 ] \033[34m1080p\n\033[33m[ 4 ] \033[34m720p\n\033[33m[ 5 ] \033[34m480p\n\033[33m[ 6 ] \033[34m360p\n\033[33m[ 7 ] \033[34m240p\n\033[33m[ 8 ] \033[34m144p\n> \033[m'))
                                                if opt_download > 8 or opt_download < 0:
                                                    print('\n\033[31m> Invalid option.\033[m\n')
                                                    continue
                                                if opt_download == 0:
                                                    break
                                                print(f'\n\033[34m> Downloading \033[31m{ytb.title}\033[34m... \033[33mPlease, wait.\033[m')
                                                if opt_download == 1:
                                                    YouTube(url).streams.get_by_itag('313').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('251').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.webm'),
                                                    "-i", 
                                                    path.join('audio.webm'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.webm')
                                                    remove('audio.webm')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                elif opt_download == 2:
                                                    YouTube(url).streams.get_by_itag('271').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('251').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.webm'),
                                                    "-i", 
                                                    path.join('audio.webm'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.webm')
                                                    remove('audio.webm')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                elif opt_download == 3:
                                                    YouTube(url).streams.get_by_itag('137').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                elif opt_download == 4:
                                                    if YouTube(url).streams.get_by_itag('22') in ytb.streams:
                                                        YouTube(url).streams.get_by_itag('22').download()
                                                        print('\n\033[32m> Download Completed.\033[m\n')
                                                        if platform == 'win32' or platform == 'win64':
                                                            rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        elif platform == 'linux':
                                                            rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        break
                                                    else:
                                                        YouTube(url).streams.get_by_itag('136').download(filename='video')
                                                        YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                        print('\n\033[32m> Download Completed.\033[m\n')
                                                        print('\n\033[34m> Starting Merging...\033[m\n')
                                                        sleep(2.5)
                                                        call(["ffmpeg", "-i",
                                                        path.join('video.mp4'),
                                                        "-i", 
                                                        path.join('audio.mp4'),
                                                        path.join(f'{ytb.title}.mp4')
                                                        ])
                                                        remove('video.mp4')
                                                        remove('audio.mp4')
                                                        if platform == 'win32' or platform == 'win64':
                                                            rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        elif platform == 'linux':
                                                            rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        break
                                                elif opt_download == 5:
                                                    YouTube(url).streams.get_by_itag('135').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                elif opt_download == 6:
                                                    if YouTube(url).streams.get_by_itag('18') in ytb.streams:
                                                        YouTube(url).streams.get_by_itag('18').download()
                                                        print('\n\033[32m> Download Completed.\033[m\n')
                                                        if platform == 'win32' or platform == 'win64':
                                                            rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        elif platform == 'linux':
                                                            rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        break
                                                    else:
                                                        YouTube(url).streams.get_by_itag('134').download(filename='video')
                                                        YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                        print('\n\033[32m> Download Completed.\033[m\n')
                                                        print('\n\033[34m> Starting Merging...\033[m\n')
                                                        sleep(2.5)
                                                        call(["ffmpeg", "-i",
                                                        path.join('video.mp4'),
                                                        "-i", 
                                                        path.join('audio.mp4'),
                                                        path.join(f'{ytb.title}.mp4')
                                                        ])
                                                        remove('video.mp4')
                                                        remove('audio.mp4')
                                                        if platform == 'win32' or platform == 'win64':
                                                            rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        elif platform == 'linux':
                                                            rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        break
                                                elif opt_download == 7:
                                                    YouTube(url).streams.get_by_itag('133').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                elif opt_download == 8:
                                                    YouTube(url).streams.get_by_itag('160').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                            elif ytb.streams.get_by_itag('271') and ytb.streams.get_by_itag('137') and ytb.streams.get_by_itag('136') and ytb.streams.get_by_itag('135') and ytb.streams.get_by_itag('134') and ytb.streams.get_by_itag('133') and ytb.streams.get_by_itag('160') in ytb.streams:
                                                opt_download = int(input('\033[33m[ 0 ] \033[33mCancel\n\033[33m[ 1 ] \033[34m1440p\n\033[33m[ 2 ] \033[34m1080p\n\033[33m[ 3 ] \033[34m720p\n\033[33m[ 4 ] \033[34m480p\n\033[33m[ 5 ] \033[34m360p\n\033[33m[ 6 ] \033[34m240p\n\033[33m[ 7 ] \033[34m144p\n> \033[m'))
                                                if opt_download > 7 or opt_download < 0:
                                                    print('\n\033[31m> Invalid option.\033[m\n')
                                                    continue
                                                if opt_download == 0:
                                                    break
                                                print(f'\n\033[34m> Downloading \033[31m{ytb.title}\033[34m... \033[33mPlease, wait.\033[m')
                                                if opt_download == 1:
                                                    YouTube(url).streams.get_by_itag('271').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('251').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.webm'),
                                                    "-i", 
                                                    path.join('audio.webm'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.webm')
                                                    remove('audio.webm')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                elif opt_download == 2:
                                                    YouTube(url).streams.get_by_itag('137').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                elif opt_download == 3:
                                                    if YouTube(url).streams.get_by_itag('22') in ytb.streams:
                                                        YouTube(url).streams.get_by_itag('22').download()
                                                        print('\n\033[32m> Download Completed.\033[m\n')
                                                        if platform == 'win32' or platform == 'win64':
                                                            rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        elif platform == 'linux':
                                                            rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        break
                                                    else:
                                                        YouTube(url).streams.get_by_itag('136').download(filename='video')
                                                        YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                        print('\n\033[32m> Download Completed.\033[m\n')
                                                        print('\n\033[34m> Starting Merging...\033[m\n')
                                                        sleep(2.5)
                                                        call(["ffmpeg", "-i",
                                                        path.join('video.mp4'),
                                                        "-i", 
                                                        path.join('audio.mp4'),
                                                        path.join(f'{ytb.title}.mp4')
                                                        ])
                                                        remove('video.mp4')
                                                        remove('audio.mp4')
                                                        if platform == 'win32' or platform == 'win64':
                                                            rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        elif platform == 'linux':
                                                            rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        break
                                                elif opt_download == 4:
                                                    YouTube(url).streams.get_by_itag('135').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                elif opt_download == 5:
                                                    if YouTube(url).streams.get_by_itag('18') in ytb.streams:
                                                        YouTube(url).streams.get_by_itag('18').download()
                                                        print('\n\033[32m> Download Completed.\033[m\n')
                                                        if platform == 'win32' or platform == 'win64':
                                                            rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        elif platform == 'linux':
                                                            rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        break
                                                    else:
                                                        YouTube(url).streams.get_by_itag('134').download(filename='video')
                                                        YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                        print('\n\033[32m> Download Completed.\033[m\n')
                                                        print('\n\033[34m> Starting Merging...\033[m\n')
                                                        sleep(2.5)
                                                        call(["ffmpeg", "-i",
                                                        path.join('video.mp4'),
                                                        "-i", 
                                                        path.join('audio.mp4'),
                                                        path.join(f'{ytb.title}.mp4')
                                                        ])
                                                        remove('video.mp4')
                                                        remove('audio.mp4')
                                                        if platform == 'win32' or platform == 'win64':
                                                            rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        elif platform == 'linux':
                                                            rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        break
                                                elif opt_download == 6:
                                                    YouTube(url).streams.get_by_itag('133').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                elif opt_download == 7:
                                                    YouTube(url).streams.get_by_itag('160').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                            elif ytb.streams.get_by_itag('137') and ytb.streams.get_by_itag('136') and ytb.streams.get_by_itag('135') and ytb.streams.get_by_itag('134') and ytb.streams.get_by_itag('133') and ytb.streams.get_by_itag('160') in ytb.streams:
                                                opt_download = int(input('\033[33m[ 0 ] \033[33mCancel\n\033[33m[ 1 ] \033[34m1080p\n\033[33m[ 2 ] \033[34m720p\n\033[33m[ 3 ] \033[34m480p\n\033[33m[ 4 ] \033[34m360p\n\033[33m[ 5 ] \033[34m240p\n\033[33m[ 6 ] \033[34m144p\n> \033[m'))
                                                if opt_download > 6 or opt_download < 0:
                                                    print('\n\033[31m> Invalid option.\033[m\n')
                                                    continue
                                                if opt_download == 0:
                                                    break
                                                print(f'\n\033[34m> Downloading \033[31m{ytb.title}\033[34m... \033[33mPlease, wait.\033[m')
                                                if opt_download == 1:
                                                    YouTube(url).streams.get_by_itag('137').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                elif opt_download == 2:
                                                    if YouTube(url).streams.get_by_itag('22') in ytb.streams:
                                                        YouTube(url).streams.get_by_itag('22').download()
                                                        print('\n\033[32m> Download Completed.\033[m\n')
                                                        if platform == 'win32' or platform == 'win64':
                                                            rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        elif platform == 'linux':
                                                            rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        break
                                                    else:
                                                        YouTube(url).streams.get_by_itag('136').download(filename='video')
                                                        YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                        print('\n\033[32m> Download Completed.\033[m\n')
                                                        print('\n\033[34m> Starting Merging...\033[m\n')
                                                        sleep(2.5)
                                                        call(["ffmpeg", "-i",
                                                        path.join('video.mp4'),
                                                        "-i", 
                                                        path.join('audio.mp4'),
                                                        path.join(f'{ytb.title}.mp4')
                                                        ])
                                                        remove('video.mp4')
                                                        remove('audio.mp4')
                                                        if platform == 'win32' or platform == 'win64':
                                                            rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        elif platform == 'linux':
                                                            rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        break
                                                elif opt_download == 3:
                                                    YouTube(url).streams.get_by_itag('135').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                elif opt_download == 4:
                                                    if YouTube(url).streams.get_by_itag('18') in ytb.streams:
                                                        YouTube(url).streams.get_by_itag('18').download()
                                                        print('\n\033[32m> Download Completed.\033[m\n')
                                                        if platform == 'win32' or platform == 'win64':
                                                            rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        elif platform == 'linux':
                                                            rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        break
                                                    else:
                                                        YouTube(url).streams.get_by_itag('134').download(filename='video')
                                                        YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                        print('\n\033[32m> Download Completed.\033[m\n')
                                                        print('\n\033[34m> Starting Merging...\033[m\n')
                                                        sleep(2.5)
                                                        call(["ffmpeg", "-i",
                                                        path.join('video.mp4'),
                                                        "-i", 
                                                        path.join('audio.mp4'),
                                                        path.join(f'{ytb.title}.mp4')
                                                        ])
                                                        remove('video.mp4')
                                                        remove('audio.mp4')
                                                        if platform == 'win32' or platform == 'win64':
                                                            rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        elif platform == 'linux':
                                                            rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        break
                                                elif opt_download == 5:
                                                    YouTube(url).streams.get_by_itag('133').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                elif opt_download == 6:
                                                    YouTube(url).streams.get_by_itag('160').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                            elif ytb.streams.get_by_itag('136') and ytb.streams.get_by_itag('135') and ytb.streams.get_by_itag('134') and ytb.streams.get_by_itag('133') and ytb.streams.get_by_itag('160') in ytb.streams:
                                                opt_download = int(input('\033[33m[ 0 ] \033[33mCancel\n\033[33m[ 1 ] \033[34m720p\n\033[33m[ 2 ] \033[34m480p\n\033[33m[ 3 ] \033[34m360p\n\033[33m[ 4 ] \033[34m240p\n\033[33m[ 5 ] \033[34m144p\n> \033[m'))
                                                if opt_download > 5 or opt_download < 0:
                                                    print('\n\033[31m> Invalid option.\033[m\n')
                                                    continue
                                                if opt_download == 0:
                                                    break
                                                print(f'\n\033[34m> Downloading \033[31m{ytb.title}\033[34m... \033[33mPlease, wait.\033[m')
                                                if opt_download == 1:
                                                    if YouTube(url).streams.get_by_itag('22') in ytb.streams:
                                                        YouTube(url).streams.get_by_itag('22').download()
                                                        print('\n\033[32m> Download Completed.\033[m\n')
                                                        if platform == 'win32' or platform == 'win64':
                                                            rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        elif platform == 'linux':
                                                            rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        break
                                                    else:
                                                        YouTube(url).streams.get_by_itag('136').download(filename='video')
                                                        YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                        print('\n\033[32m> Download Completed.\033[m\n')
                                                        print('\n\033[34m> Starting Merging...\033[m\n')
                                                        sleep(2.5)
                                                        call(["ffmpeg", "-i",
                                                        path.join('video.mp4'),
                                                        "-i", 
                                                        path.join('audio.mp4'),
                                                        path.join(f'{ytb.title}.mp4')
                                                        ])
                                                        remove('video.mp4')
                                                        remove('audio.mp4')
                                                        if platform == 'win32' or platform == 'win64':
                                                            rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        elif platform == 'linux':
                                                            rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        break
                                                elif opt_download == 2:
                                                    YouTube(url).streams.get_by_itag('135').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                elif opt_download == 3:
                                                    if YouTube(url).streams.get_by_itag('18') in ytb.streams:
                                                        YouTube(url).streams.get_by_itag('18').download()
                                                        print('\n\033[32m> Download Completed.\033[m\n')
                                                        if platform == 'win32' or platform == 'win64':
                                                            rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        elif platform == 'linux':
                                                            rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        break
                                                    else:
                                                        YouTube(url).streams.get_by_itag('134').download(filename='video')
                                                        YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                        print('\n\033[32m> Download Completed.\033[m\n')
                                                        print('\n\033[34m> Starting Merging...\033[m\n')
                                                        sleep(2.5)
                                                        call(["ffmpeg", "-i",
                                                        path.join('video.mp4'),
                                                        "-i", 
                                                        path.join('audio.mp4'),
                                                        path.join(f'{ytb.title}.mp4')
                                                        ])
                                                        remove('video.mp4')
                                                        remove('audio.mp4')
                                                        if platform == 'win32' or platform == 'win64':
                                                            rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        elif platform == 'linux':
                                                            rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        break
                                                elif opt_download == 4:
                                                    YouTube(url).streams.get_by_itag('133').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                elif opt_download == 5:
                                                    YouTube(url).streams.get_by_itag('160').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                            elif ytb.streams.get_by_itag('135') and ytb.streams.get_by_itag('134') and ytb.streams.get_by_itag('133') and ytb.streams.get_by_itag('160') in ytb.streams:
                                                opt_download = int(input('\033[33m[ 0 ] \033[33mCancel\n\033[33m[ 1 ] \033[34m480p\n\033[33m[ 2 ] \033[34m360p\n\033[33m[ 3 ] \033[34m240p\n\033[33m[ 4 ] \033[34m144p\n> \033[m'))
                                                if opt_download > 4 or opt_download < 0:
                                                    print('\n\033[31m> Invalid option.\033[m\n')
                                                    continue
                                                if opt_download == 0:
                                                    break
                                                print(f'\n\033[34m> Downloading \033[31m{ytb.title}\033[34m... \033[33mPlease, wait.\033[m')
                                                if opt_download == 1:
                                                    YouTube(url).streams.get_by_itag('135').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                elif opt_download == 2:
                                                    if YouTube(url).streams.get_by_itag('18') in ytb.streams:
                                                        YouTube(url).streams.get_by_itag('18').download()
                                                        print('\n\033[32m> Download Completed.\033[m\n')
                                                        if platform == 'win32' or platform == 'win64':
                                                            rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        elif platform == 'linux':
                                                            rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        break
                                                    else:
                                                        YouTube(url).streams.get_by_itag('134').download(filename='video')
                                                        YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                        print('\n\033[32m> Download Completed.\033[m\n')
                                                        print('\n\033[34m> Starting Merging...\033[m\n')
                                                        sleep(2.5)
                                                        call(["ffmpeg", "-i",
                                                        path.join('video.mp4'),
                                                        "-i", 
                                                        path.join('audio.mp4'),
                                                        path.join(f'{ytb.title}.mp4')
                                                        ])
                                                        remove('video.mp4')
                                                        remove('audio.mp4')
                                                        if platform == 'win32' or platform == 'win64':
                                                            rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        elif platform == 'linux':
                                                            rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        break
                                                elif opt_download == 3:
                                                    YouTube(url).streams.get_by_itag('133').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                elif opt_download == 4:
                                                    YouTube(url).streams.get_by_itag('160').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                            elif ytb.streams.get_by_itag('134') and ytb.streams.get_by_itag('133') and ytb.streams.get_by_itag('160') in ytb.streams:
                                                opt_download = int(input('\033[33m[ 0 ] \033[33mCancel\n\033[33m[ 1 ] \033[34m360p\n\033[33m[ 2 ] \033[34m240p\n\033[33m[ 3 ] \033[34m144p\n> \033[m'))
                                                if opt_download > 3 or opt_download < 0:
                                                    print('\n\033[31m> Invalid option.\033[m\n')
                                                    continue
                                                if opt_download == 0:
                                                    break
                                                print(f'\n\033[34m> Downloading \033[31m{ytb.title}\033[34m... \033[33mPlease, wait.\033[m')
                                                if opt_download == 1:
                                                    if YouTube(url).streams.get_by_itag('18') in ytb.streams:
                                                        YouTube(url).streams.get_by_itag('18').download()
                                                        print('\n\033[32m> Download Completed.\033[m\n')
                                                        if platform == 'win32' or platform == 'win64':
                                                            rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        elif platform == 'linux':
                                                            rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        break
                                                    else:
                                                        YouTube(url).streams.get_by_itag('134').download(filename='video')
                                                        YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                        print('\n\033[32m> Download Completed.\033[m\n')
                                                        print('\n\033[34m> Starting Merging...\033[m\n')
                                                        sleep(2.5)
                                                        call(["ffmpeg", "-i",
                                                        path.join('video.mp4'),
                                                        "-i", 
                                                        path.join('audio.mp4'),
                                                        path.join(f'{ytb.title}.mp4')
                                                        ])
                                                        remove('video.mp4')
                                                        remove('audio.mp4')
                                                        if platform == 'win32' or platform == 'win64':
                                                            rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        elif platform == 'linux':
                                                            rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                        break
                                                elif opt_download == 2:
                                                    YouTube(url).streams.get_by_itag('133').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                elif opt_download == 3:
                                                    YouTube(url).streams.get_by_itag('160').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                            elif ytb.streams.get_by_itag('133') and ytb.streams.get_by_itag('160') in ytb.streams:
                                                opt_download = int(input('\033[33m[ 0 ] \033[33mCancel\n\033[33m[ 1 ] \033[34m240p\n\033[33m[ 2 ] \033[34m144p\n> \033[m'))
                                                if opt_download > 2 or opt_download < 0:
                                                    print('\033[31m> Invalid option.\033[m')
                                                    continue
                                                if opt_download == 0:
                                                    break
                                                print(f'\n\033[34m> Downloading \033[31m{ytb.title}\033[34m... \033[33mPlease, wait.\033[m')
                                                if opt_download == 1:
                                                    YouTube(url).streams.get_by_itag('133').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                elif opt_download == 2:
                                                    YouTube(url).streams.get_by_itag('160').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                            elif ytb.streams.get_by_itag('160') in ytb.streams:
                                                opt_download = int(input('\033[33m[ 0 ] \033[33mCancel\n\033[33m[ 1 ] \033[34m144p\n> \033[m'))
                                                if opt_download > 1 or opt_download < 0:
                                                    print('\n\033[31m> Invalid option.\033[m\n')
                                                    continue
                                                if opt_download == 0:
                                                    break
                                                print(f'\n\033[34m> Downloading \033[31m{ytb.title}\033[34m... \033[33mPlease, wait.\033[m')
                                                if opt_download == 1:
                                                    YouTube(url).streams.get_by_itag('160').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                            else:
                                                print('\n\033[31m> An unknown error has occurred.\033[m')
                                                break
                                        except error.HTTPError:
                                            print('\n\033[31m> This file is unavailable for download, please choose another.\033[m\n')
                                            continue
                                        except FileExistsError:
                                            print('\n\033[31m> The file already exists.\033[m')
                                            remove(f'{ytb.title}.mp4')
                                            break   
                                        except:
                                            print('\n\033[31m> An unknown error has occurred.\033[m\n')
                                            break
                            elif opt_format60 == 3:
                                try:
                                    if ytb.streams.get_by_itag('140') in ytb.streams:
                                        print(f'\n\033[34m> Downloading \033[31m{ytb.title}\033[34m... \033[33mPlease, wait.\033[m')
                                        YouTube(url).streams.get_by_itag('140').download(filename='music')
                                        print('\n\033[32m> Download Completed.\033[m')
                                        print('\n\033[34m> Starting Conversion...\033[m\n')
                                        sleep(2.5)
                                        call(["ffmpeg", "-i",
                                        path.join('music.mp4'),
                                        path.join('music.mp3')
                                        ])
                                        remove('music.mp4')
                                        sleep(0.5)
                                        rename('music.mp3', f'{ytb.title}.mp3')
                                        sleep(0.5)
                                        if platform == 'win32' or platform == 'win64':
                                            rename(f'{ytb.title}.mp3', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp3')
                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                        elif platform == 'linux':
                                            rename(f'{ytb.title}.mp3', f'/home/{getuser()}/Downloads/{ytb.title}.mp3')
                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                        break
                                    elif opt_format60 == 0:
                                        print('\033[m')
                                        break
                                    else:
                                        print('\033[31m> Invalid option.\033[m')
                                        continue
                                    break
                                except error.HTTPError:
                                    print('\n\033[31m> This file is unavailable for download, please choose another.\033[m\n')
                                    continue
                                except FileExistsError:
                                    print('\n\033[31m> The file already exists.\033[m')
                                    if opt_format60 == 3:
                                        remove(f'{ytb.title}.mp3')
                                    else:
                                        remove(f'{ytb.title}.mp4')
                                    break   
                                except:
                                    print('\n\033[31m> An unknown error has occurred.\033[m\n')
                                    break
                        else:
                            opt_format30 = int(input('\033[33m[ 0 ] Cancel\n\033[33m[ 1 ] \033[34mVideo\n\033[33m[ 2 ] \033[34mAudio \033[33m(128 Kbps)\033[34m\n> \033[m'))
                            print('\033[33m='*50,'\n')
                            # 30FPS
                            if opt_format30 == 1:
                                while True:
                                    try:
                                        if ytb.streams.get_by_itag('313') and ytb.streams.get_by_itag('271') and ytb.streams.get_by_itag('137') and ytb.streams.get_by_itag('136') and ytb.streams.get_by_itag('135') and ytb.streams.get_by_itag('134') and ytb.streams.get_by_itag('133') and ytb.streams.get_by_itag('160') in ytb.streams:
                                            opt_download = int(input('\033[33m[ 0 ] \033[33mCancel\n\033[33m[ 1 ] \033[34m2160p\n\033[33m[ 2 ] \033[34m1440p\n\033[33m[ 3 ] \033[34m1080p\n\033[33m[ 4 ] \033[34m720p\n\033[33m[ 5 ] \033[34m480p\n\033[33m[ 6 ] \033[34m360p\n\033[33m[ 7 ] \033[34m240p\n\033[33m[ 8 ] \033[34m144p\n> \033[m'))
                                            if opt_download > 8 or opt_download < 0:
                                                print('\n\033[31m> Invalid option.\033[m\n')
                                                continue
                                            if opt_download == 0:
                                                break
                                            print(f'\n\033[34m> Downloading \033[31m{ytb.title}\033[34m... \033[33mPlease, wait.\033[m')
                                            if opt_download == 1:
                                                YouTube(url).streams.get_by_itag('313').download(filename='video')
                                                YouTube(url).streams.get_by_itag('251').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.webm'),
                                                "-i", 
                                                path.join('audio.webm'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.webm')
                                                remove('audio.webm')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 2:
                                                YouTube(url).streams.get_by_itag('271').download(filename='video')
                                                YouTube(url).streams.get_by_itag('251').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.webm'),
                                                "-i", 
                                                path.join('audio.webm'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.webm')
                                                remove('audio.webm')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 3:
                                                YouTube(url).streams.get_by_itag('137').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 4:
                                                if YouTube(url).streams.get_by_itag('22') in ytb.streams:
                                                    YouTube(url).streams.get_by_itag('22').download()
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                else:
                                                    YouTube(url).streams.get_by_itag('136').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                            elif opt_download == 5:
                                                YouTube(url).streams.get_by_itag('135').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 6:
                                                if YouTube(url).streams.get_by_itag('18') in ytb.streams:
                                                    YouTube(url).streams.get_by_itag('18').download()
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                else:
                                                    YouTube(url).streams.get_by_itag('134').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                            elif opt_download == 7:
                                                YouTube(url).streams.get_by_itag('133').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 8:
                                                YouTube(url).streams.get_by_itag('160').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                        elif ytb.streams.get_by_itag('271') and ytb.streams.get_by_itag('137') and ytb.streams.get_by_itag('136') and ytb.streams.get_by_itag('135') and ytb.streams.get_by_itag('134') and ytb.streams.get_by_itag('133') and ytb.streams.get_by_itag('160') in ytb.streams:
                                            opt_download = int(input('\033[33m[ 0 ] \033[33mCancel\n\033[33m[ 1 ] \033[34m1440p\n\033[33m[ 2 ] \033[34m1080p\n\033[33m[ 3 ] \033[34m720p\n\033[33m[ 4 ] \033[34m480p\n\033[33m[ 5 ] \033[34m360p\n\033[33m[ 6 ] \033[34m240p\n\033[33m[ 7 ] \033[34m144p\n> \033[m'))
                                            if opt_download > 7 or opt_download < 0:
                                                print('\n\033[31m> Invalid option.\033[m\n')
                                                continue
                                            if opt_download == 0:
                                                break
                                            print(f'\n\033[34m> Downloading \033[31m{ytb.title}\033[34m... \033[33mPlease, wait.\033[m')
                                            if opt_download == 1:
                                                YouTube(url).streams.get_by_itag('271').download(filename='video')
                                                YouTube(url).streams.get_by_itag('251').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.webm'),
                                                "-i", 
                                                path.join('audio.webm'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.webm')
                                                remove('audio.webm')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 2:
                                                YouTube(url).streams.get_by_itag('137').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 3:
                                                if YouTube(url).streams.get_by_itag('22') in ytb.streams:
                                                    YouTube(url).streams.get_by_itag('22').download()
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                else:
                                                    YouTube(url).streams.get_by_itag('136').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                            elif opt_download == 4:
                                                YouTube(url).streams.get_by_itag('135').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 5:
                                                if YouTube(url).streams.get_by_itag('18') in ytb.streams:
                                                    YouTube(url).streams.get_by_itag('18').download()
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                else:
                                                    YouTube(url).streams.get_by_itag('134').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                            elif opt_download == 6:
                                                YouTube(url).streams.get_by_itag('133').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 7:
                                                YouTube(url).streams.get_by_itag('160').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                        elif ytb.streams.get_by_itag('137') and ytb.streams.get_by_itag('136') and ytb.streams.get_by_itag('135') and ytb.streams.get_by_itag('134') and ytb.streams.get_by_itag('133') and ytb.streams.get_by_itag('160') in ytb.streams:
                                            opt_download = int(input('\033[33m[ 0 ] \033[33mCancel\n\033[33m[ 1 ] \033[34m1080p\n\033[33m[ 2 ] \033[34m720p\n\033[33m[ 3 ] \033[34m480p\n\033[33m[ 4 ] \033[34m360p\n\033[33m[ 5 ] \033[34m240p\n\033[33m[ 6 ] \033[34m144p\n> \033[m'))
                                            if opt_download > 6 or opt_download < 0:
                                                print('\n\033[31m> Invalid option.\033[m\n')
                                                continue
                                            if opt_download == 0:
                                                break
                                            print(f'\n\033[34m> Downloading \033[31m{ytb.title}\033[34m... \033[33mPlease, wait.\033[m')
                                            if opt_download == 1:
                                                YouTube(url).streams.get_by_itag('137').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 2:
                                                if YouTube(url).streams.get_by_itag('22') in ytb.streams:
                                                    YouTube(url).streams.get_by_itag('22').download()
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                else:
                                                    YouTube(url).streams.get_by_itag('136').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                            elif opt_download == 3:
                                                YouTube(url).streams.get_by_itag('135').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 4:
                                                if YouTube(url).streams.get_by_itag('18') in ytb.streams:
                                                    YouTube(url).streams.get_by_itag('18').download()
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                else:
                                                    YouTube(url).streams.get_by_itag('134').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                            elif opt_download == 5:
                                                YouTube(url).streams.get_by_itag('133').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 6:
                                                YouTube(url).streams.get_by_itag('160').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                        elif ytb.streams.get_by_itag('136') and ytb.streams.get_by_itag('135') and ytb.streams.get_by_itag('134') and ytb.streams.get_by_itag('133') and ytb.streams.get_by_itag('160') in ytb.streams:
                                            opt_download = int(input('\033[33m[ 0 ] \033[33mCancel\n\033[33m[ 1 ] \033[34m720p\n\033[33m[ 2 ] \033[34m480p\n\033[33m[ 3 ] \033[34m360p\n\033[33m[ 4 ] \033[34m240p\n\033[33m[ 5 ] \033[34m144p\n> \033[m'))
                                            if opt_download > 5 or opt_download < 0:
                                                print('\n\033[31m> Invalid option.\033[m\n')
                                                continue
                                            if opt_download == 0:
                                                break
                                            print(f'\n\033[34m> Downloading \033[31m{ytb.title}\033[34m... \033[33mPlease, wait.\033[m')
                                            if opt_download == 1:
                                                if YouTube(url).streams.get_by_itag('22') in ytb.streams:
                                                    YouTube(url).streams.get_by_itag('22').download()
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                else:
                                                    YouTube(url).streams.get_by_itag('136').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                            elif opt_download == 2:
                                                YouTube(url).streams.get_by_itag('135').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 3:
                                                if YouTube(url).streams.get_by_itag('18') in ytb.streams:
                                                    YouTube(url).streams.get_by_itag('18').download()
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                else:
                                                    YouTube(url).streams.get_by_itag('134').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                            elif opt_download == 4:
                                                YouTube(url).streams.get_by_itag('133').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 5:
                                                YouTube(url).streams.get_by_itag('160').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                        elif ytb.streams.get_by_itag('135') and ytb.streams.get_by_itag('134') and ytb.streams.get_by_itag('133') and ytb.streams.get_by_itag('160') in ytb.streams:
                                            opt_download = int(input('\033[33m[ 0 ] \033[33mCancel\n\033[33m[ 1 ] \033[34m480p\n\033[33m[ 2 ] \033[34m360p\n\033[33m[ 3 ] \033[34m240p\n\033[33m[ 4 ] \033[34m144p\n> \033[m'))
                                            if opt_download > 4 or opt_download < 0:
                                                print('\n\033[31m> Invalid option.\033[m\n')
                                                continue
                                            if opt_download == 0:
                                                break
                                            print(f'\n\033[34m> Downloading \033[31m{ytb.title}\033[34m... \033[33mPlease, wait.\033[m')
                                            if opt_download == 1:
                                                YouTube(url).streams.get_by_itag('135').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 2:
                                                if YouTube(url).streams.get_by_itag('18') in ytb.streams:
                                                    YouTube(url).streams.get_by_itag('18').download()
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                else:
                                                    YouTube(url).streams.get_by_itag('134').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                            elif opt_download == 3:
                                                YouTube(url).streams.get_by_itag('133').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 4:
                                                YouTube(url).streams.get_by_itag('160').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                        elif ytb.streams.get_by_itag('134') and ytb.streams.get_by_itag('133') and ytb.streams.get_by_itag('160') in ytb.streams:
                                            opt_download = int(input('\033[33m[ 0 ] \033[33mCancel\n\033[33m[ 1 ] \033[34m360p\n\033[33m[ 2 ] \033[34m240p\n\033[33m[ 3 ] \033[34m144p\n> \033[m'))
                                            if opt_download > 3 or opt_download < 0:
                                                print('\n\033[31m> Invalid option.\033[m\n')
                                                continue
                                            if opt_download == 0:
                                                break
                                            print(f'\n\033[34m> Downloading \033[31m{ytb.title}\033[34m... \033[33mPlease, wait.\033[m')
                                            if opt_download == 1:
                                                if YouTube(url).streams.get_by_itag('18') in ytb.streams:
                                                    YouTube(url).streams.get_by_itag('18').download()
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                                else:
                                                    YouTube(url).streams.get_by_itag('134').download(filename='video')
                                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                    print('\n\033[32m> Download Completed.\033[m\n')
                                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                                    sleep(2.5)
                                                    call(["ffmpeg", "-i",
                                                    path.join('video.mp4'),
                                                    "-i", 
                                                    path.join('audio.mp4'),
                                                    path.join(f'{ytb.title}.mp4')
                                                    ])
                                                    remove('video.mp4')
                                                    remove('audio.mp4')
                                                    if platform == 'win32' or platform == 'win64':
                                                        rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    elif platform == 'linux':
                                                        rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                        print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                    break
                                            elif opt_download == 2:
                                                YouTube(url).streams.get_by_itag('133').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 3:
                                                YouTube(url).streams.get_by_itag('160').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                        elif ytb.streams.get_by_itag('133') and ytb.streams.get_by_itag('160') in ytb.streams:
                                            opt_download = int(input('\033[33m[ 0 ] \033[33mCancel\n\033[33m[ 1 ] \033[34m240p\n\033[33m[ 2 ] \033[34m144p\n> \033[m'))
                                            if opt_download > 2 or opt_download < 0:
                                                print('\033[31m> Invalid option.\033[m')
                                                continue
                                            if opt_download == 0:
                                                break
                                            print(f'\n\033[34m> Downloading \033[31m{ytb.title}\033[34m... \033[33mPlease, wait.\033[m')
                                            if opt_download == 1:
                                                YouTube(url).streams.get_by_itag('133').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                            elif opt_download == 2:
                                                YouTube(url).streams.get_by_itag('160').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                        elif ytb.streams.get_by_itag('160') in ytb.streams:
                                            opt_download = int(input('\033[33m[ 0 ] \033[33mCancel\n\033[33m[ 1 ] \033[34m144p\n> \033[m'))
                                            if opt_download > 1 or opt_download < 0:
                                                print('\n\033[31m> Invalid option.\033[m\n')
                                                continue
                                            if opt_download == 0:
                                                break
                                            print(f'\n\033[34m> Downloading \033[31m{ytb.title}\033[34m... \033[33mPlease, wait.\033[m')
                                            if opt_download == 1:
                                                YouTube(url).streams.get_by_itag('160').download(filename='video')
                                                YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                                print('\n\033[32m> Download Completed.\033[m\n')
                                                print('\n\033[34m> Starting Merging...\033[m\n')
                                                sleep(2.5)
                                                call(["ffmpeg", "-i",
                                                path.join('video.mp4'),
                                                "-i", 
                                                path.join('audio.mp4'),
                                                path.join(f'{ytb.title}.mp4')
                                                ])
                                                remove('video.mp4')
                                                remove('audio.mp4')
                                                if platform == 'win32' or platform == 'win64':
                                                    rename(f'{ytb.title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                elif platform == 'linux':
                                                    rename(f'{ytb.title}.mp4', f'/home/{getuser()}/Downloads/{ytb.title}.mp4')
                                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                                break
                                        else:
                                            print('\n\033[31m> An unknown error has occurred.\033[m')
                                            break
                                    except error.HTTPError:
                                        print('\n\033[31m> This file is unavailable for download, please choose another.\033[m\n')
                                        continue
                                    except FileExistsError:
                                        print('\n\033[31m> The file already exists.\033[m')
                                        remove(f'{ytb.title}.mp4')
                                        break   
                                    except:
                                        print('\n\033[31m> An unknown error has occurred.\033[m\n')
                                        break
                            elif opt_format30 == 2:
                                try:
                                    if ytb.streams.get_by_itag('140') in ytb.streams:
                                        print(f'\n\033[34m> Downloading \033[31m{ytb.title}\033[34m... \033[33mPlease, wait.\033[m')
                                        YouTube(url).streams.get_by_itag('140').download(filename='music')
                                        print('\n\033[32m> Download Completed.\033[m')
                                        print('\n\033[34m> Starting Conversion...\033[m\n')
                                        sleep(2.5)
                                        call(["ffmpeg", "-i",
                                        path.join('music.mp4'),
                                        path.join('music.mp3')
                                        ])
                                        remove('music.mp4')
                                        sleep(0.5)
                                        rename('music.mp3', f'{ytb.title}.mp3')
                                        sleep(0.5)
                                        if platform == 'win32' or platform == 'win64':
                                            rename(f'{ytb.title}.mp3', f'C:\\Users\\{getuser()}\\Downloads\\{ytb.title}.mp3')
                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                        elif platform == 'linux':
                                            rename(f'{ytb.title}.mp3', f'/home/{getuser()}/Downloads/{ytb.title}.mp3')
                                            print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                        break
                                    elif opt_format30 == 0:
                                        print('\033[m')
                                        break
                                    else:
                                        print('\033[31m> Invalid option.\033[m')
                                        continue
                                    break
                                except error.HTTPError:
                                    print('\n\033[31m> This file is unavailable for download, please choose another.\033[m\n')
                                    continue
                                except FileExistsError:
                                    print('\n\033[31m> The file already exists.\033[m')
                                    remove(f'{ytb.title}.mp3')
                                    break   
                                except:
                                    print('\n\033[31m> An unknown error has occurred.\033[m\n')
                                    break
                        break
                    except:
                        print('\033[m')
                        break
            elif opt_type == 2:
                try:
                    playlist = Playlist(url)
                    playlist._video_regex = compile(r"\"url\":\"(/watch\?v=[\w-]*)")
                    print(f'\n\n\033[33mVideos in the following playlist: \033[34m{len(playlist.video_urls)}\033[m')
                    print('\033[33m='*50)
                    while True:
                        opt_pl = int(input('\n\033[33m[ 0 ] Cancel\n\033[33m[ 1 ] \033[34mVideo\n\033[33m[ 2 ] \033[34mMusic\n> \033[m'))
                        print('\033[33m='*50)
                        if opt_pl > 2 or opt_pl < 0:
                            print('\n\033[31m> Invalid option.\033[m')
                            continue
                        elif opt_pl == 1:
                            for video in playlist.video_urls:
                                print(f'\n\033[34m> Downloading \033[31m{YouTube(video).title}\033[34m... \033[33mPlease, wait.\033[m')
                                YouTube(video).streams.get_highest_resolution().download()
                                if i == 0:
                                    print(f'\n\033[32m> {i} Download Completed.\033[m')
                                else:
                                    print(f'\n\033[32m> {i} Downloads Completed.\033[m')
                                if platform == 'win32' or platform == 'win64':
                                    rename(f'{YouTube(video).title}.mp4', f'C:\\Users\\{getuser()}\\Downloads\\{YouTube(video).title}.mp4')
                                elif platform == 'linux':
                                    rename(f'{YouTube(video).title}.mp4', f'/home/{getuser()}/Downloads/{YouTube(video).title}.mp4')
                                if i == len(playlist.video_urls):
                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                i += 1
                        elif opt_pl == 2:
                            for music in playlist.video_urls:
                                print(f'\n\033[34m> Downloading \033[31m{YouTube(music).title}\033[34m... \033[33mPlease, wait.\033[m')
                                YouTube(music).streams.get_audio_only().download(filename=f'music{i}')
                                if i == 0:
                                    print(f'\n\033[32m> {i} Download Completed.\033[m')
                                else:
                                    print(f'\n\033[32m> {i} Downloads Completed.\033[m')
                                print('\n\033[34m> Starting Conversion...\033[m\n')
                                sleep(2.5)
                                call(["ffmpeg", "-i",
                                path.join(f'music{i}.mp4'),
                                path.join(f'music{i}.mp3')
                                ])
                                remove(f'music{i}.mp4')
                                sleep(0.5)
                                rename(f'music{i}.mp3', f'{YouTube(music).title}.mp3')
                                sleep(0.5)
                                if platform == 'win32' or platform == 'win64':
                                    rename(f'{YouTube(music).title}.mp3', f'C:\\Users\\{getuser()}\\Downloads\\{YouTube(music).title}.mp3')
                                elif platform == 'linux':
                                    rename(f'{YouTube(music).title}.mp3', f'/home/{getuser()}/Downloads/{YouTube(music).title}.mp3')
                                if i == len(playlist.video_urls):
                                    print('\n\033[34m> Downloaded files moved to Downloads folder.\033[m')
                                i += 1
                        elif opt_pl == 0:
                            print('\033[m')
                            break
                        break
                except FileExistsError:
                    print('\n\033[31m> The file already exists.\033[m')
                    if opt_pl == 1:
                        remove(f'{YouTube(video).title}.mp4')
                    elif opt_pl == 2:
                        remove(f'{YouTube(music).title}.mp3')
                    break
            print('\n\033[33mThanks for using.\033[m\n')
            break

    class main:
        print('\n\033[34mCoded by f4ll_py\033[m')
        print('\n\033[34mVersion: \033[31m0.3\033[m')
        print('''    \033[31m       _ \033[39m     _                     _                 _           
    \033[31m _   _| |_\033[39m __| | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
    \033[31m| | | | __\033[39m/ _` |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
    \033[31m| |_| | || \033[39m(_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
    \033[31m \__, |\__\033[39m\__,_|\___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
    \033[31m |___/''')
        while True:
            try:
                url = str(input('\n\033[34m> Insert the link: \033[m'))
                yt(url)
                break
            except KeyError:
                print('\n\033[31m> An error with the cipher has ocurred. See documentation in Github to resolve.\033[m\n')
                break
            except KeyboardInterrupt:
                print('\n\n\033[33mThanks for using.\033[m\n')
                break
            except:
                print('\n\033[31m> An unknown error has occurred.\033[m\n')
                break
