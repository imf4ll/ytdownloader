# videodownloader 0.1

<img src="https://i.imgur.com/Sls6pOV.gif">

**IF YOU HAVE ANOTHER PYTHON VERSION BEYOND Python 3, USE 'python3' BEFORE THE PARAMETERS**

**THE FILES GOES TO SCRIPT FOLDER**

**SOMETIMES 720p AND 360p DON'T NEED POS-PROCESSING**

Dependencies:
- Python 3
- pytube3
- <a href="https://ffmpeg.zeranoe.com/builds/">FFmpeg</a>

Documentation:
- Install dependencies:
  - pip install -r dependencies.txt

- Valid parameters:
  python videodownloader.py

Termux:
  - pkg install ffmpeg
  - mv extract.py -f /data/data/files/use/lib/python3.8/site-packages/pytube/
  - pip3 install --update pytube3

Linux:
  - sudo apt install ffmpeg
  - pip3 install --update pytube3
  - Move the extract.py to pytube folder in site-packages

Known Issues:
- pytube:
  - ImportError: cannot import name 'quote' from 'pytube.compat' : Install pytube3 with 'pip install -r dependencies.txt'
  - KeyError: Cipher : Go for 'C:\Users\{Your Username Here}\AppData\Local\Programs\Python\Python38\Lib\site-packages\pytube' and replace 'extract.py' with <a href="https://github.com/f4ll-py/videodownloader/tree/master/issuecorrection">that 'extract.py'</a>
- FFmpeg: If your FFmpeg is not recognized by terminal, try <a href="http://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/#:~:text=If%20you%20try%20that%20right,and%20it%27ll%20understand%20us.">this</a>.
