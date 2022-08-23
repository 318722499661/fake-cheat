# Fake cheat
A fake ghost client. I dosen't do anything. Used to troll your freinds and tell them you are **HaCkInG** 

## Not launching
This is because I programmed it to only launch if minecraft is open. However, that only works on linux/macos.
That means on windows it will not launch even if minecraft is open. To fix that refer to the comment in the **main.py** file

## Dependencies
You will need the pygame python package for it to work

## How to build
Run these commands:
```
pip install pygame
pip install pyinstaller
python -m PyInstaller --icon=logo.ico --noconsole --onefile main.py
```
then copy the fonts and images folders into the dist directory and then you can run the file in the dist directory

If you get an error that says you do not have pip refer to this: https://pip.pypa.io/en/stable/installation/
# Screenshots
<img src="https://raw.githubusercontent.com/CloudyWhale/fake-cheat/master/screenshots/screenshot1.png" alt="screenshot 1">
Video: https://streamable.com/ge639o
