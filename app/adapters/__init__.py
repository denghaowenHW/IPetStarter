from log import logger
from auth import auth_bp


def init_module(app):
    app.register_blueprint(auth_bp)
    logger.info('initialize adapters module')

