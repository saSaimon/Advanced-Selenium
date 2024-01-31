import os
import logging

def setup_logging():
    # Create Logs directory if it doesn't exist
    logs_dir = 'Logs'
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    # Create a logger
    logger = logging.getLogger('behave_logger')
    logger.setLevel(logging.DEBUG)  # Capture all logs of DEBUG level and above

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Create file handler which logs all messages in file
    fh = logging.FileHandler(os.path.join(logs_dir, 'test_automation.log'))
    fh.setLevel(logging.DEBUG)  # Set to DEBUG to capture all levels of logs
    fh.setFormatter(formatter)

    # Create console handler which logs all messages in console
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)  # Set to DEBUG to capture all levels of logs
    ch.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(fh)
    # logger.addHandler(ch)

    return logger
