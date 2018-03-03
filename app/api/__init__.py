from flask import Blueprint, request
from flask_restplus import Api
from setuptools import find_packages
import os
from importlib import import_module
from log import logger
import sys
from datetime import datetime

bp = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(bp, version='1.0', title='IPetStarter Service API', description='For IPet Client')


def init_module(app):
    app.register_blueprint(bp)
    for module_name in find_packages(os.path.dirname(os.path.abspath(__file__))):
        module = import_module('.%s' % module_name, package=__name__)
        if hasattr(module, 'init_module'):
            module.init_module(api)
            logger.info('initialize api module')


@api.errorhandler
def default_handler_error(error):
    exc_info = sys.exc_info()
    if exc_info[1] is None:
        exc_info = None
        logger.error('Exception on %s [%s]', request.path, request.method, exc_info=exc_info)
        return {'error': 'internal server error', 'message': error.message}


@bp.before_request
def before_request():
    request.start_time = datetime.now()
