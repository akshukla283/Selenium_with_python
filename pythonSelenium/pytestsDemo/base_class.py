import inspect
import logging


class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        # loggerName will give form which method it is getting called and
        # place in __name__ so we can replace this

        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile5.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        # filehandler object
        logger.setLevel(logging.DEBUG)

        return logger