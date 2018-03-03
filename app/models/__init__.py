from app.models.base import db
from log import logger


def init_module(app):
    logger.info('initialize models module')
    db.init_app(app)
