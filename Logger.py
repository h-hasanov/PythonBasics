import logging

#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s-%(levelname)s-%(message)s', level=logging.DEBUG)

logging.info("About to start the program")
logging.debug("The value of the configuration item is found in config.jsn")
logging.error("This is a spurious error that will likely drive people nuts")

logger = logging.getLogger("MyCustomLogger")
fh = logging.FileHandler("myCustomLogger.log")
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
logger.error("This is an error")

logging.error("This error does not go to the file")


try:
    thisIsNotGoingToWork = 1/0
except Exception as e:
    logging.error("Exception occured", exc_info=True)
    

logging.error("This is another error")