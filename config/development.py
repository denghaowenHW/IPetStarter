from default import DefaultConfig


class DevelopmentConfig(DefaultConfig):
    MONGODB_HOST = '192.168.1.218'
    MONGODB_DB = 'ipet_starter'
