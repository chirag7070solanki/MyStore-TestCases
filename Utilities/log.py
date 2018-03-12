import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler('Logfile.log', mode='w')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)


def starttestcase():
    logger.info('******************************************************************************************')
    logger.info("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  TestCase Started   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    logger.info("******************************************************************************************")


def endtestcase():
    logger.info("******************************************************************************************")
    logger.info("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  TestCase Ended   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    logger.info("******************************************************************************************")


def info(msg):
    logger.info(msg)


def error(msg):
    logger.error(msg)


def debug(msg):
    logger.debug(msg)


def warning(msg):
    logger.warn(msg)


def critical(msg):
    logger.critical(msg)
