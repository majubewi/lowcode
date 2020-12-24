
import logging
from logging.handlers import RotatingFileHandler
from rich.logging import RichHandler

FILEPATH = "logging/rich-useage-log.txt"

# Remove previous logfile
try:
    import os
    os.remove(FILEPATH)
except:
    pass

# Console log handler
FORMAT = "%(asctime)s - %(name)s - [%(levelname)s] - %(filename)s, %(lineno)d, %(funcName)s: %(message)s"
richhandler = RichHandler()
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[richhandler]
)
log = logging.getLogger("test")

# Add file log handler
MAX_BYTES = 10000000 # Maximum size for a log file
BACKUP_COUNT = 9 # Maximum number of old log files
filehandler = RotatingFileHandler(FILEPATH, maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT)
filehandler.setFormatter(logging.Formatter(FORMAT))
filehandler.setLevel(logging.DEBUG)
log.addHandler(filehandler)

# Default logging
log.info("Hello, World!")

# Stack traces log
a = 5
b = 0
try:
  c = a / b
except Exception as e:
  log.error("Exception occurred", exc_info=True)

# Disable logging to file => It is not possible to remove the stdout handler.
log.removeHandler(filehandler)
