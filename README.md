# ytdownloader 0.5

![Downloads](https://img.shields.io/github/downloads/f4ll-py/ytdownloader/total)
![LastCommit](https://img.shields.io/github/last-commit/f4ll-py/ytdownloader)
![Issues](https://img.shields.io/github/issues/f4ll-py/ytdownloader)
![PullRequests](https://img.shields.io/github/issues-pr/f4ll-py/ytdownloader)
![Followers](https://img.shields.io/github/followers/f4ll-py?label=Follow)

<img src="https://i.imgur.com/PFr5ejx.gif">

**IF YOU HAVE ANOTHER PYTHON VERSION BEYOND Python 3, USE 'python3' BEFORE THE PARAMETERS**

Changelog 0.5:
- Complete refactor for a more stable and scalable application

**IF YOU WANT TERMINAL APP: <a href="https://github.com/f4ll-py/ytdownloader/tree/ytdownloader_0.3b">Click here</a>**

Dependencies:
- Python 3
- pytube3
- PySimpleGUI
- <a href="https://ffmpeg.org/download.html#build-windows">FFmpeg</a>

Documentation:

  - Windows:
    - Install <a href="https://ffmpeg.org/download.html#build-windows">ffmpeg</a>
    - Add ffmpeg.exe to windows path ( <a href="http://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/#:~:text=If%20you%20try%20that%20right,and%20it%27ll%20understand%20us.">tutorial</a> )
    - pip3 install -r dependencies.txt
    - Move 'extract.py' in folder issuecorrection, to pytube folder (normally in "C:\Users\{Username}\AppData\Local\Programs\Python\Python38\Lib\site-packages\pytube")
    - Run script in terminal a with 'python ytdownloader.py'.
  - Linux:
    - sudo apt install ffmpeg
    - pip3 install -r requirements.txt
    - Open terminal in 'issuecorrection', mv extract.py -f /home/{Your Username here}/.local/lib/python3.8/site-packages/pytube/
    - Run script in terminal a with 'python3 ytdownloader.py'

Known Issues:
- pytube:
  - ImportError: cannot import name 'quote' from 'pytube.compat' : Install pytube3 with 'pip install -r requirements.txt'
  - KeyError: Cipher : Go for 'C:\Users\{Your Username Here}\AppData\Local\Programs\Python\Python38\Lib\site-packages\pytube' and replace 'extract.py' with <a href="https://github.com/f4ll-py/videodownloader/tree/master/issuecorrection">that 'extract.py'</a>
- FFmpeg: If your FFmpeg is not recognized by terminal, try <a href="http://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/#:~:text=If%20you%20try%20that%20right,and%20it%27ll%20understand%20us.">this</a>.
