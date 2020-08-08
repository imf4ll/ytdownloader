# ytdownloader 0.4

<img src="https://i.imgur.com/PFr5ejx.gif">

**IF YOU HAVE ANOTHER PYTHON VERSION BEYOND Python 3, USE 'python3' BEFORE THE PARAMETERS**

**I CONSIDERED THE IDEA OF ADDING A GRAPHICAL INTERFACE, BUT THE ERRORS THAT RETURN ARE IRREVERSIBLE AND THE MOST IMPORTANT PLUGIN IS IGNORED BY SCRIPT**

**SOMETIMES 720p AND 360p DON'T NEED POS-PROCESSING**

Changelog 0.4:
- Graphical Interface added ( For now simple );
- Biggest change in code because GUI.

**IF YOU WANT TERMINAL APP: <a href="https://github.com/f4ll-py/ytdownloader/tree/4d2b4565ad9fca2868849c1966033fcd0d925f4d">Click here</a>**

Dependencies:
- Python 3
- pytube3
- PySimpleGUI
- <a href="https://ffmpeg.zeranoe.com/builds/">FFmpeg</a>

Documentation:
- Install dependencies:
  - pip install -r dependencies.txt

- Install <a href="https://ffmpeg.zeranoe.com/builds/">FFmpeg</a> static.
  - In Windows, for your terminal recognize, install <a href="http://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/#:~:text=If%20you%20try%20that%20right,and%20it%27ll%20understand%20us.">this</a>.
  - In Termux or Linux, the steps are below.

- Valid parameters:
  python ytdownloader.py

Termux:
  - pkg install ffmpeg
  - pip3 install --update pytube3  
  - In folder 'issuecorrection', mv extract.py -f /data/data/files/usr/lib/python3.8/site-packages/pytube/
  
Linux:
  - sudo apt install ffmpeg
  - pip3 install --update pytube3
  - Open terminal in 'issuecorrection', mv extract.py -f /home/{Your Username here}/.local/lib/python3.8/site-packages/pytube/

Known Issues:
- pytube:
  - ImportError: cannot import name 'quote' from 'pytube.compat' : Install pytube3 with 'pip install -r dependencies.txt'
  - KeyError: Cipher : Go for 'C:\Users\{Your Username Here}\AppData\Local\Programs\Python\Python38\Lib\site-packages\pytube' and replace 'extract.py' with <a href="https://github.com/f4ll-py/videodownloader/tree/master/issuecorrection">that 'extract.py'</a>
- FFmpeg: If your FFmpeg is not recognized by terminal, try <a href="http://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/#:~:text=If%20you%20try%20that%20right,and%20it%27ll%20understand%20us.">this</a>.
