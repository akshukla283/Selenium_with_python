import logging
# logging present default in python


#  to generate testcase name need to use __name__ it will capture testcase file name
# it is mandatory to pass in logging
def test_loggingDemo():

    logger = logging.getLogger(__name__)
    # if don't give '__name__' it will take as root
    # it will print in file, there is handler to manage that what format, what file and all

    # below is from parent logging
    fileHandler = logging.FileHandler('logfile.log')

    # for logging message format in file, suppose we have below sample
    # 2019-02-17 12:40:14,789 : ERROR: <testcasename>: Fatal error in submitting credit card payment on step 4. cannot continue
    # here you can see that message has been separated by ":" and added
    # time : level : name: message

    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s : %(message)s")
    # we have formated in tuple so that in run time it can evaluate and print
    # now we have to form connection so that logger get format information
    # adding formatter in to file handler
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # filehandler object
    # need to set level to see log based on debug, warning, error, etc
    logger.setLevel(logging.INFO)
    # here we set 'info' level so message will be logged from info to critical
    # we can use debug also that create more steps and all

    logger.debug("A debug statement is executed")
    logger.info("Information statements ")
    logger.warning("Something is in warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical issue")

    # above logger level are default level
    # if want to see only error log then set level 'error' you will see error and critical level message there
    # whatever level we set, we get message from that level to last level

    # if we add 'debug' level again after some level it will not print that message