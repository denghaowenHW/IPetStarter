from default import DefaultConfig


class DevelopmentConfig(DefaultConfig):
    MONGODB_HOST = '127.0.0.1'
    MONGODB_DB = 'ipet_starter'
