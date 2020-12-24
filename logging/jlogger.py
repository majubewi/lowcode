import logging
from logging.handlers import RotatingFileHandler
from rich.logging import RichHandler

class JLogger:
    def __init__(self,name, filepath = None, remove_previous_file = False):
        """
        If you set no filepath there will be no file logging.
        """
    
        if(remove_previous_file):
            try:
                import os
                os.remove(filepath)
            except:
                pass

        format = "[%(name)s] - %(filename)s, %(lineno)d, %(funcName)s: %(message)s"
        richhandler = RichHandler()
        logging.basicConfig(
            level=logging.DEBUG, format=format, datefmt="[%X]", handlers=[richhandler]
        )
        self.logger = logging.getLogger(name)
        
        if(filepath != None):
            # Add file log handler
            MAX_BYTES = 10000000 # Maximum size for a log file
            BACKUP_COUNT = 9 # Maximum number of old log files
            filehandler = RotatingFileHandler(filepath, maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT)
            fileformat = "%(asctime)s - [%(name)s] - [%(levelname)s] - %(filename)s, %(lineno)d, %(funcName)s: %(message)s"
            filehandler.setFormatter(logging.Formatter(fileformat))
            filehandler.setLevel(logging.DEBUG)
            self.logger.addHandler(filehandler)

    def getLogger(self):
        return self.logger
