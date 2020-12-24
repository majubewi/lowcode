from jlogger import JLogger

# If you set no filepath there will be no file logging.
log = JLogger(name = "test",filepath="logging/jlogger-usage-log.txt",remove_previous_file = False).getLogger()
log.info("This is a info message.")

