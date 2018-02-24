import os
from logging.config import fileConfig
from config import load_config


# create logs dir at current path
if not os.path.exists('logs'):
    os.mkdir('logs')

# init logs
fileConfig(os.path.join(os.path.dirname(__file__)), '..', 'logging.ini', disable_existing_loggers=False)
config = load_config()
