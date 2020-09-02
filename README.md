# ytdownloader 0.3b

![Downloads](https://img.shields.io/github/downloads/f4ll-py/ytdownloader/total)
![LastCommit](https://img.shields.io/github/last-commit/f4ll-py/ytdownloader)
![Issues](https://img.shields.io/github/issues/f4ll-py/ytdownloader)
![PullRequests](https://img.shields.io/github/issues-pr/f4ll-py/ytdownloader)
![Followers](https://img.shields.io/github/followers/f4ll-py?label=Follow)

<img src="https://i.imgur.com/y1WKgQj.png">

**IF YOU HAVE ANOTHER PYTHON VERSION BEYOND Python 3, USE 'python3' BEFORE THE PARAMETERS**

**SOMETIMES 720p AND 360p DON'T NEED POS-PROCESSING**

Changelog 0.3b:
- Last update of terminal app;
- Some changes in code.

Dependencies:
- Python 3
- pytube3
- <a href="https://ffmpeg.zeranoe.com/builds/">FFmpeg</a>

Documentation:

  - Windows:
    - Install <a href="https://ffmpeg.zeranoe.com/builds/">ffmpeg</a>
    - Add ffmpeg.exe to windows path ( <a href="http://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/#:~:text=If%20you%20try%20that%20right,and%20it%27ll%20understand%20us.">tutorial</a> )
    - pip3 install -r dependencies.txt
    - Move 'extract.py' in folder issuecorrection, to pytube folder ( normally in "C:\Users\{Username}\AppData\Local\Programs\Python\Python38\Lib\site-packages\pytube" )
    - Run script in terminal a with 'python ytdownloader.py'.
  - Linux:
    - sudo apt install ffmpeg
    - pip3 install -r dependencies.txt
    - Open terminal in 'issuecorrection', mv extract.py -f /home/{Your Username here}/.local/lib/python3.8/site-packages/pytube/
    - Run script in terminal a with 'python3 ytdownloader.py'

Known Issues:
- pytube:
  - ImportError: cannot import name 'quote' from 'pytube.compat' : Install pytube3 with 'pip install -r dependencies.txt'
  - KeyError: Cipher : Go for 'C:\Users\{Your Username Here}\AppData\Local\Programs\Python\Python38\Lib\site-packages\pytube' and replace 'extract.py' with <a href="https://github.com/f4ll-py/videodownloader/tree/master/issuecorrection">that 'extract.py'</a>
- FFmpeg: If your FFmpeg is not recognized by terminal, try <a href="http://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/#:~:text=If%20you%20try%20that%20right,and%20it%27ll%20understand%20us.">this</a>.
