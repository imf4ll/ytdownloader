#!/usr/bin/env python3
try:
    from pytube import YouTube, Stream
    from subprocess import call
    from os import path, remove
    from time import sleep
except Exception as e:
    print()
    print(f'\033[31mError with a module: {e}\033[m')
    print("\033[31mTry 'pip install -r dependencies.txt' to install all modules.\033[m")
    print()
else:
    def yt(url):
        while True:
            try:
                while True:
                    ytb = YouTube(url)
                    print('\n\n')
                    print(f'\033[33mTitle: \033[34m{ytb.title}\033[m')
                    print(f'\033[33mAuthor: \033[34m{ytb.author}\033[m')
                    print(f'\033[33mLength: \033[34m{ytb.length/60:.0f} minutes.\033[m')
                    print('\033[33m='*108,'\n')
                    opt_format = int(input('\033[33m[ 0 ] Cancel\n\033[33m[ 1 ] \033[34mVideo\n\033[33m[ 2 ] \033[34mAudio (128 Kbps)\n> \033[m'))
                    print('\033[33m='*108,'\n')

                    if opt_format == 1:
                        while True:
                            if ytb.streams.get_by_itag('137') and ytb.streams.get_by_itag('136') and ytb.streams.get_by_itag('135') and ytb.streams.get_by_itag('134') and ytb.streams.get_by_itag('133') and ytb.streams.get_by_itag('160') in ytb.streams:
                                opt_download = int(input('\033[33m[ 1 ] \033[33m1080p\n\033[33m[ 2 ] \033[34m720p\n\033[33m[ 3 ] \033[34m480p\n\033[33m[ 4 ] \033[34m360p\n\033[33m[ 5 ] \033[34m240p\n\033[33m[ 6 ] \033[34m144p\n> \033[m'))
                                if opt_download > 6 or opt_download < 1:
                                    print('\n\033[31m> Invalid option.\033[m\n')
                                    continue
                                print('\n\033[34m> Downloading... \033[33mPlease, wait.\033[m')
                                if opt_download == 1:
                                    YouTube(url).streams.get_by_itag('137').download(filename='video')
                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                    print('\n\033[32m> Download Completed.\033[m\n')
                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                    sleep(4)
                                    call(["ffmpeg", "-i",
                                    path.join('video.mp4'),
                                    "-i", 
                                    path.join('audio.mp4'),
                                    path.join(f'{ytb.title}.mp4')
                                    ])
                                    remove('video.mp4')
                                    remove('audio.mp4')
                                    break
                                elif opt_download == 2:
                                    if YouTube(url).streams.get_by_itag('22') in ytb.streams:
                                        YouTube(url).streams.get_by_itag('22').download()
                                        print('\n\033[32m> Download Completed.\033[m\n')
                                        break
                                    else:
                                        YouTube(url).streams.get_by_itag('136').download(filename='video')
                                        YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                        print('\n\033[32m> Download Completed.\033[m\n')
                                        print('\n\033[34m> Starting Merging...\033[m\n')
                                        sleep(4)
                                        call(["ffmpeg", "-i",
                                        path.join('video.mp4'),
                                        "-i", 
                                        path.join('audio.mp4'),
                                        path.join(f'{ytb.title}.mp4')
                                        ])
                                        remove('video.mp4')
                                        remove('audio.mp4')
                                        break
                                elif opt_download == 3:
                                    YouTube(url).streams.get_by_itag('135').download(filename='video')
                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                    print('\n\033[32m> Download Completed.\033[m\n')
                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                    sleep(4)
                                    call(["ffmpeg", "-i",
                                    path.join('video.mp4'),
                                    "-i", 
                                    path.join('audio.mp4'),
                                    path.join(f'{ytb.title}.mp4')
                                    ])
                                    remove('video.mp4')
                                    remove('audio.mp4')
                                    break
                                elif opt_download == 4:
                                    if YouTube(url).streams.get_by_itag('18') in ytb.streams:
                                        YouTube(url).streams.get_by_itag('18').download()
                                        print('\n\033[32m> Download Completed.\033[m\n')
                                        break
                                    else:
                                        YouTube(url).streams.get_by_itag('134').download(filename='video')
                                        YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                        print('\n\033[32m> Download Completed.\033[m\n')
                                        print('\n\033[34m> Starting Merging...\033[m\n')
                                        sleep(4)
                                        call(["ffmpeg", "-i",
                                        path.join('video.mp4'),
                                        "-i", 
                                        path.join('audio.mp4'),
                                        path.join(f'{ytb.title}.mp4')
                                        ])
                                        remove('video.mp4')
                                        remove('audio.mp4')
                                        break
                                elif opt_download == 5:
                                    YouTube(url).streams.get_by_itag('133').download(filename='video')
                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                    print('\n\033[32m> Download Completed.\033[m\n')
                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                    sleep(4)
                                    call(["ffmpeg", "-i",
                                    path.join('video.mp4'),
                                    "-i", 
                                    path.join('audio.mp4'),
                                    path.join(f'{ytb.title}.mp4')
                                    ])
                                    remove('video.mp4')
                                    remove('audio.mp4')
                                    break
                                elif opt_download == 6:
                                    YouTube(url).streams.get_by_itag('160').download(filename='video')
                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                    print('\n\033[32m> Download Completed.\033[m\n')
                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                    sleep(4)
                                    call(["ffmpeg", "-i",
                                    path.join('video.mp4'),
                                    "-i", 
                                    path.join('audio.mp4'),
                                    path.join(f'{ytb.title}.mp4')
                                    ])
                                    remove('video.mp4')
                                    remove('audio.mp4')
                                    break
                            elif ytb.streams.get_by_itag('136') and ytb.streams.get_by_itag('135') and ytb.streams.get_by_itag('134') and ytb.streams.get_by_itag('133') and ytb.streams.get_by_itag('160') in ytb.streams:
                                opt_download = int(input('\033[33m[ 1 ] \033[33m720p\n\033[33m[ 2 ] \033[34m480p\n\033[33m[ 3 ] \033[34m360p\n\033[33m[ 4 ] \033[34m240p\n\033[33m[ 5 ] \033[34m144p\n> \033[m'))
                                if opt_download > 5 or opt_download < 1:
                                    print('\n\033[31m> Invalid option.\033[m\n')
                                    continue
                                print('\n\033[34m> Downloading... \033[33mPlease, wait.\033[m')
                                if opt_download == 1:
                                    if YouTube(url).streams.get_by_itag('22') in ytb.streams:
                                        YouTube(url).streams.get_by_itag('22').download()
                                        print('\n\033[32m> Download Completed.\033[m\n')
                                        break
                                    else:
                                        YouTube(url).streams.get_by_itag('136').download(filename='video')
                                        YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                        print('\n\033[32m> Download Completed.\033[m\n')
                                        print('\n\033[34m> Starting Merging...\033[m\n')
                                        sleep(4)
                                        call(["ffmpeg", "-i",
                                        path.join('video.mp4'),
                                        "-i", 
                                        path.join('audio.mp4'),
                                        path.join(f'{ytb.title}.mp4')
                                        ])
                                        remove('video.mp4')
                                        remove('audio.mp4')
                                        break
                                elif opt_download == 2:
                                    YouTube(url).streams.get_by_itag('135').download(filename='video')
                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                    print('\n\033[32m> Download Completed.\033[m\n')
                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                    sleep(4)
                                    call(["ffmpeg", "-i",
                                    path.join('video.mp4'),
                                    "-i", 
                                    path.join('audio.mp4'),
                                    path.join(f'{ytb.title}.mp4')
                                    ])
                                    remove('video.mp4')
                                    remove('audio.mp4')
                                    break
                                elif opt_download == 3:
                                    if YouTube(url).streams.get_by_itag('18') in ytb.streams:
                                        YouTube(url).streams.get_by_itag('18').download()
                                        print('\n\033[32m> Download Completed.\033[m\n')
                                        break
                                    else:
                                        YouTube(url).streams.get_by_itag('134').download(filename='video')
                                        YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                        print('\n\033[32m> Download Completed.\033[m\n')
                                        print('\n\033[34m> Starting Merging...\033[m\n')
                                        sleep(4)
                                        call(["ffmpeg", "-i",
                                        path.join('video.mp4'),
                                        "-i", 
                                        path.join('audio.mp4'),
                                        path.join(f'{ytb.title}.mp4')
                                        ])
                                        remove('video.mp4')
                                        remove('audio.mp4')
                                        break
                                elif opt_download == 4:
                                    YouTube(url).streams.get_by_itag('133').download(filename='video')
                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                    print('\n\033[32m> Download Completed.\033[m\n')
                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                    sleep(4)
                                    call(["ffmpeg", "-i",
                                    path.join('video.mp4'),
                                    "-i", 
                                    path.join('audio.mp4'),
                                    path.join(f'{ytb.title}.mp4')
                                    ])
                                    remove('video.mp4')
                                    remove('audio.mp4')
                                    break
                                elif opt_download == 5:
                                    YouTube(url).streams.get_by_itag('160').download(filename='video')
                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                    print('\n\033[32m> Download Completed.\033[m\n')
                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                    sleep(4)
                                    call(["ffmpeg", "-i",
                                    path.join('video.mp4'),
                                    "-i", 
                                    path.join('audio.mp4'),
                                    path.join(f'{ytb.title}.mp4')
                                    ])
                                    remove('video.mp4')
                                    remove('audio.mp4')
                                    break
                            elif ytb.streams.get_by_itag('135') and ytb.streams.get_by_itag('134') and ytb.streams.get_by_itag('133') and ytb.streams.get_by_itag('160') in ytb.streams:
                                opt_download = int(input('\033[33m[ 1 ] \033[33m480p\n\033[33m[ 2 ] \033[34m360p\n\033[33m[ 3 ] \033[34m240p\n\033[33m[ 4 ] \033[34m144p\n> \033[m'))
                                if opt_download > 4 or opt_download < 1:
                                    print('\n\033[31m> Invalid option.\033[m\n')
                                    continue
                                print('\n\033[34m> Downloading... \033[33mPlease, wait.\033[m')
                                if opt_download == 1:
                                    YouTube(url).streams.get_by_itag('135').download(filename='video')
                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                    print('\n\033[32m> Download Completed.\033[m\n')
                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                    sleep(4)
                                    call(["ffmpeg", "-i",
                                    path.join('video.mp4'),
                                    "-i", 
                                    path.join('audio.mp4'),
                                    path.join(f'{ytb.title}.mp4')
                                    ])
                                    remove('video.mp4')
                                    remove('audio.mp4')
                                    break
                                elif opt_download == 2:
                                    if YouTube(url).streams.get_by_itag('18') in ytb.streams:
                                        YouTube(url).streams.get_by_itag('18').download()
                                        print('\n\033[32m> Download Completed.\033[m\n')
                                        break
                                    else:
                                        YouTube(url).streams.get_by_itag('134').download(filename='video')
                                        YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                        print('\n\033[32m> Download Completed.\033[m\n')
                                        print('\n\033[34m> Starting Merging...\033[m\n')
                                        sleep(4)
                                        call(["ffmpeg", "-i",
                                        path.join('video.mp4'),
                                        "-i", 
                                        path.join('audio.mp4'),
                                        path.join(f'{ytb.title}.mp4')
                                        ])
                                        remove('video.mp4')
                                        remove('audio.mp4')
                                        break
                                elif opt_download == 3:
                                    YouTube(url).streams.get_by_itag('133').download(filename='video')
                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                    print('\n\033[32m> Download Completed.\033[m\n')
                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                    sleep(4)
                                    call(["ffmpeg", "-i",
                                    path.join('video.mp4'),
                                    "-i", 
                                    path.join('audio.mp4'),
                                    path.join(f'{ytb.title}.mp4')
                                    ])
                                    remove('video.mp4')
                                    remove('audio.mp4')
                                    break
                                elif opt_download == 4:
                                    YouTube(url).streams.get_by_itag('160').download(filename='video')
                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                    print('\n\033[32m> Download Completed.\033[m\n')
                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                    sleep(4)
                                    call(["ffmpeg", "-i",
                                    path.join('video.mp4'),
                                    "-i", 
                                    path.join('audio.mp4'),
                                    path.join(f'{ytb.title}.mp4')
                                    ])
                                    remove('video.mp4')
                                    remove('audio.mp4')
                                    break
                            elif ytb.streams.get_by_itag('134') and ytb.streams.get_by_itag('133') and ytb.streams.get_by_itag('160') in ytb.streams:
                                opt_download = int(input('\033[33m[ 1 ] \033[33m360p\n\033[33m[ 2 ] \033[34m240p\n\033[33m[ 3 ] \033[34m144p\n> \033[m'))
                                if opt_download > 3 or opt_download < 1:
                                    print('\n\033[31m> Invalid option.\033[m\n')
                                    continue
                                print('\n\033[34m> Downloading... \033[33mPlease, wait.\033[m')
                                if opt_download == 1:
                                    if YouTube(url).streams.get_by_itag('18') in ytb.streams:
                                        YouTube(url).streams.get_by_itag('18').download()
                                        print('\n\033[32m> Download Completed.\033[m\n')
                                        break
                                    else:
                                        YouTube(url).streams.get_by_itag('134').download(filename='video')
                                        YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                        print('\n\033[32m> Download Completed.\033[m\n')
                                        print('\n\033[34m> Starting Merging...\033[m\n')
                                        sleep(4)
                                        call(["ffmpeg", "-i",
                                        path.join('video.mp4'),
                                        "-i", 
                                        path.join('audio.mp4'),
                                        path.join(f'{ytb.title}.mp4')
                                        ])
                                        remove('video.mp4')
                                        remove('audio.mp4')
                                        break
                                elif opt_download == 2:
                                    YouTube(url).streams.get_by_itag('133').download(filename='video')
                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                    print('\n\033[32m> Download Completed.\033[m\n')
                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                    sleep(4)
                                    call(["ffmpeg", "-i",
                                    path.join('video.mp4'),
                                    "-i", 
                                    path.join('audio.mp4'),
                                    path.join(f'{ytb.title}.mp4')
                                    ])
                                    remove('video.mp4')
                                    remove('audio.mp4')
                                    break
                                elif opt_download == 3:
                                    YouTube(url).streams.get_by_itag('160').download(filename='video')
                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                    print('\n\033[32m> Download Completed.\033[m\n')
                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                    sleep(4)
                                    call(["ffmpeg", "-i",
                                    path.join('video.mp4'),
                                    "-i", 
                                    path.join('audio.mp4'),
                                    path.join(f'{ytb.title}.mp4')
                                    ])
                                    remove('video.mp4')
                                    remove('audio.mp4')
                                    break
                            elif ytb.streams.get_by_itag('133') and ytb.streams.get_by_itag('160') in ytb.streams:
                                opt_download = int(input('\033[33m[ 1 ] \033[33m240p\n\033[33m[ 2 ] \033[34m144p\n> \033[m'))
                                if opt_download > 2 or opt_download < 1:
                                    print('\033[31m> Invalid option.\033[m')
                                    continue
                                print('\n\033[34m> Downloading... \033[33mPlease, wait.\033[m')
                                if opt_download == 1:
                                    YouTube(url).streams.get_by_itag('133').download(filename='video')
                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                    print('\n\033[32m> Download Completed.\033[m\n')
                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                    sleep(4)
                                    call(["ffmpeg", "-i",
                                    path.join('video.mp4'),
                                    "-i", 
                                    path.join('audio.mp4'),
                                    path.join(f'{ytb.title}.mp4')
                                    ])
                                    remove('video.mp4')
                                    remove('audio.mp4')
                                    break
                                elif opt_download == 2:
                                    YouTube(url).streams.get_by_itag('160').download(filename='video')
                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                    print('\n\033[32m> Download Completed.\033[m\n')
                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                    sleep(4)
                                    call(["ffmpeg", "-i",
                                    path.join('video.mp4'),
                                    "-i", 
                                    path.join('audio.mp4'),
                                    path.join(f'{ytb.title}.mp4')
                                    ])
                                    remove('video.mp4')
                                    remove('audio.mp4')
                                    break
                            elif ytb.streams.get_by_itag('160') in ytb.streams:
                                opt_download = int(input('\033[33m[ 1 ] \033[33m144p\n> \033[m'))
                                if opt_download > 1 or opt_download < 1:
                                    print('\n\033[31m> Invalid option.\033[m\n')
                                    continue
                                print('\n\033[34m> Downloading... \033[33mPlease, wait.\033[m')
                                if opt_download == 1:
                                    YouTube(url).streams.get_by_itag('160').download(filename='video')
                                    YouTube(url).streams.get_by_itag('140').download(filename='audio')
                                    print('\n\033[32m> Download Completed.\033[m\n')
                                    print('\n\033[34m> Starting Merging...\033[m\n')
                                    sleep(4)
                                    call(["ffmpeg", "-i",
                                    path.join('video.mp4'),
                                    "-i", 
                                    path.join('audio.mp4'),
                                    path.join(f'{ytb.title}.mp4')
                                    ])
                                    remove('video.mp4')
                                    remove('audio.mp4')
                                    break
                            else:
                                print('Erro')
                                break
                    elif opt_format == 2:
                        if ytb.streams.get_by_itag('140') in ytb.streams:
                            print('\n\033[34m> Downloading... \033[33mPlease, wait.\033[m')
                            YouTube(url).streams.get_by_itag('140').download()
                            print('\n\033[32m> Download Completed.\033[m')
                            print('\n\033[34m> Starting Conversion...\033[m\n')
                            sleep(4)
                            call(["ffmpeg", "-i",
                            path.join(f'{ytb.title}.mp4'),
                            path.join(f'{ytb.title}.mp3')
                            ])
                            remove(f'{ytb.title}.mp4')
                            break
                    elif opt_format == 0:
                        print('\033[m')
                        break
                    else:
                        print('\033[31m> Invalid option.\033[m')
                        continue
                    break
                break
            except KeyboardInterrupt:
                print('\n\n\033[33mThanks for using.\033[m\n')
                break

    class main:
        print('\n\033[34mCoded by f4ll_py\033[m')
        print('\n\033[34mVersion: \033[31m0.1\033[m')
        print('''\033[31m                                                                                                         
          ,--.   ,--.                 ,--.                          ,--.                  ,--.               
,--.  ,--.`--' ,-|  | ,---.  ,---.  ,-|  | ,---. ,--.   ,--.,--,--, |  | ,---.  ,--,--. ,-|  | ,---. ,--.--. 
 \  `'  / ,--.' .-. || .-. :| .-. |' .-. || .-. ||  |.'.|  ||      \|  || .-. |' ,-.  |' .-. || .-. :|  .--' 
  \    /  |  |\ `-' |\   --.' '-' '\ `-' |' '-' '|   .'.   ||  ||  ||  |' '-' '\ '-'  |\ `-' |\   --.|  |    
   `--'   `--' `---'  `----' `---'  `---'  `---' '--'   '--'`--''--'`--' `---'  `--`--' `---'  `----'`--' ''')
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
            except FileNotFoundError:
                print('\n\033[31m> Try not to download songs with characters like [] or () in name.\033[m')
            except:
                print('\n\033[31m> An unknown error has occured.\033[m\n')
                break
