# README:
# Source:   https://simber.deepjyoti30.dev/#get-started
# General problem with simber: After a critical log , he code execution stops!!!

from simber import Logger
import sys

filepath = "logging/simber-usage-log.txt"

# Delete the previous log file
import os
if os.path.exists(filepath):
  os.remove(filepath)

# Create a new instance
logger = Logger(
    name="test",
    level="INFO",
    format="{time} [%a{levelname}%][{logger}] Line {lineno}:",
    log_path=filepath,
    file_level="DEBUG",
    file_format="{time} [{levelname}][{logger}] {filename} Line {lineno}:"
)

#Set log level
logger.update_level("DEBUG")

# Print a debug statement.
logger.debug("Just a debug message")

# Print an info statement
logger.info("Just printing an info message from the test logger")

# Print a warning message
logger.warning("A warning message from the test logger")

# Print a error message
logger.error("A error message from the test logger")

#logger.critical("A critical message from the test logger")

# Disable logging to stdout
def logger_update_disable_stdout(logger, disabled = False):
  for stream in logger._streams:
    if(stream.stream.name == "<stdout>"):
      stream._disabled = True

logger_update_disable_stdout(logger,True)
logger.info("This will not be visible in stdout.")

# Disable writing to files
logger.update_disable_file(True)
logger.info("This will not be visible in either stdout or the file.")