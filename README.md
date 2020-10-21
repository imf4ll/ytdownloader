<img src="https://i.imgur.com/PFr5ejx.gif">

[![CodeFactor](https://www.codefactor.io/repository/github/ff4LL/ytdownloader/badge)](https://www.codefactor.io/repository/github/ff4LL/ytdownloader)
![LastCommit](https://img.shields.io/github/last-commit/ff4LL/ytdownloader)
![Issues](https://img.shields.io/github/issues/ff4LL/ytdownloader)
![PullRequests](https://img.shields.io/github/issues-pr/ff4LL/ytdownloader)
![Followers](https://img.shields.io/github/followers/ff4LL?label=Follow)

<br><br>

## 🤔 What is YTDownloader?
  - A tool to download YouTube videos until 144p to 4K 60FPS, musics and playlists.

<br><br>

## ☁️ Download & Install
  - Windows:
    - Install <a href="https://ffmpeg.org/download.html#build-windows">ffmpeg</a>
    - Add ffmpeg.exe to windows path ( <a href="http://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/#:~:text=If%20you%20try%20that%20right,and%20it%27ll%20understand%20us.">tutorial</a> )
    - pip3 install -r requirements.txt
    - Move 'extract.py' in folder issuecorrection, to pytube folder (normally in "C:\Users\{Username}\AppData\Local\Programs\Python\Python38\Lib\site-packages\pytube")
    - Run script in terminal a with 'python ytdownloader.py'.
  - Linux:
    - sudo apt install ffmpeg
    - pip3 install -r requirements.txt
    - Open terminal in 'issuecorrection', mv extract.py -f /home/{Your Username here}/.local/lib/python3.8/site-packages/pytube/
    - Run script in terminal a with 'python3 ytdownloader.py'

<br><br>

## ⚙️ Setup
  - Run 'python ytdownloader.py' in console to open the program.
  
<br><br>

## ❌ Known Issues:
  - pytube:
    - ImportError: cannot import name 'quote' from 'pytube.compat' : Install pytube3 with 'pip install -r requirements.txt'
    - KeyError: Cipher : Go for 'C:\Users\{Your Username Here}\AppData\Local\Programs\Python\Python38\Lib\site-packages\pytube' and replace 'extract.py' with <a href="https://github.com/f4ll-py/videodownloader/tree/master/issuecorrection">that 'extract.py'</a>
  - FFmpeg: If your FFmpeg is not recognized by terminal, try <a href="http://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/#:~:text=If%20you%20try%20that%20right,and%20it%27ll%20understand%20us.">this</a>.
