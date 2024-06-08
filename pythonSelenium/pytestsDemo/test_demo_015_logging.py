import logging
# logging present default in python


#  to generate testcase name need to use __name__ it will capture testcase file name
# it is mandatory to pass in logging
logger = logging.getLogger(__name__)
fileHandler = logging.FileHandler('logfile2.log')
formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s : %(message)s")
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
def test_loggingDemo2():
    # setting level from 'debug'
    logger.setLevel(logging.DEBUG)

    logger.debug("A debug statement is executed")
    logger.info("Information statements ")
    logger.warning("Something is in warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical issue")
