class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    JWT_ACCESS_TOKEN_EXPIRES = False
    JWT_TOKEN_LOCATION = ['headers']
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'

    

class DevelopmentConfig(Config):
    DEBUG=True
    ENV = 'development'
    DATABASE = 'report_db'
    TESTING = False


class TestingConfig(Config):
    DEBUG=True
    ENV = 'testing'
    DATABASE= 'reporttest_db'
    TESTING = True

class ProductionConfig(Config):
    DEBUG=False
    ENV = 'testing'
    TESTING = False

    

app_configuration = {
    "development":DevelopmentConfig,
    "testing":TestingConfig,
    "production":ProductionConfig
}

