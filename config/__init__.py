

def load_config():
    os = 'DEVELOPMENT'

    if os == 'DEVELOPMENT':
        from development import DevelopmentConfig
        config = DevelopmentConfig
    elif os == 'PRODUCTION':
        from production import ProductionConfig
        config = ProductionConfig
    else:
        from default import DefaultConfig
        config = DefaultConfig
    return config
