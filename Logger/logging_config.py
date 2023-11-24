import os
import logging


def setup_logging():
    # Create Logs directory if it doesn't exist
    logs_dir = 'Logs'
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    logger = logging.getLogger('behave_logger')
    logger.setLevel(logging.INFO)

    # Create file handler which logs even debug messages
    # File is now saved in the Logs directory
    fh = logging.FileHandler(os.path.join(logs_dir, 'test_automation.log'))
    fh.setLevel(logging.INFO)

    # Create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger


# def get_logger(name):
#     setup_logging()
#     logger = logging.getLogger(name)
#     return logger
