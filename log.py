import os
import logging.handlers
import sys

if not os.path.exists('logs'):
    os.mkdir('logs')
formatter = logging.Formatter('[%(asctime)s]<pid=%(process)d tid=%(thread)d>%(levelname)s - %(message)s')
file_handler = logging.handlers.RotatingFileHandler("logs/Ipet.log", maxBytes=20 * 1024 * 1024, backupCount=25)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

error_handler = logging.handlers.RotatingFileHandler("logs/IPet_error.log", maxBytes=20 * 1024*1024,backupCount=25)
error_handler.setFormatter(formatter)
error_handler.setLevel(logging.ERROR)

# create logger
logger = logging.getLogger('fLogger')
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.addHandler(error_handler)