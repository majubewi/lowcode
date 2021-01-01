#!/usr/bin/env bash

# If it does not work anymore play around with versions
sudo apt install wine
wget https://www.python.org/ftp/python/2.7.9/python-2.7.9.amd64.msi
wine msiexec /i python-2.7.9.amd64.msi /qb
sudo dpkg --add-architecture i386 && sudo apt-get update && sudo apt-get install wine32
wget https://bootstrap.pypa.io/get-pip.py
wine ~/.wine/drive_c/Python27/python.exe get-pip.py
wine ~/.wine/drive_c/Python27/python.exe -m pip install pyinstaller==3.5 #Installs pyinstaller for python 2
wine ~/.wine/drive_c/Python27/python.exe -m pip install py2exe_py2  #Installs py2exe for python 2

sudo apt install python2
python2.7 get-pip.py
python2.7 -m pip install pynput==1.0 --user