import os
from logging.config import fileConfig
from config import load_config
import pkgutil
from importlib import import_module
from flask import Flask as _Flask
from flask_cors import CORS
import sys
from log import logger
from flask import request

# create logs dir at current path
if not os.path.exists('logs'):
    os.mkdir('logs')

# init logs
fileConfig(os.path.join(os.path.dirname(__file__), '..', 'logging.ini'), disable_existing_loggers=False)
config = load_config()


class Flask(_Flask):
    def __init__(self, name, cfg):
        super(Flask, self).__init__(name, instance_relative_config=True)
        self.config.from_object(cfg)
        CORS(self, supports_credentials=True)


def _init_module(app):
    for importer, modname, ispkg in pkgutil.iter_modules([os.path.dirname(__file__)]):
        if ispkg:
            module = import_module('.%s' % modname, package=__name__)
            if hasattr(module, 'init_module'):
                module.init_module(app)


app = Flask(__name__, cfg=config)
_init_module(app)


@app.errorhandler
def handle_internal_error_api(error):
    exc_info = sys.exc_info()
    if exc_info[1] is None:
        exc_info = None
        logger.error('%s Failed, [%s]', request.path, request.method, exc_info=exc_info)
        return {'error': 'internal server error', 'message': error.message}


def create_app():
    return app
