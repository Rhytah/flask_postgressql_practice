import os

class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    JWT_ACCESS_TOKEN_EXPIRES = False
    JWT_TOKEN_LOCATION = ['headers']
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'
    DATABASE_URI = os.getenv('DATABASE_URL')
    

class DevelopmentConfig(Config):
    DEBUG=True
    ENV = 'development'
    DATABASE_URI = 'postgresql://localhost/report_db'
    TESTING = False


class TestingConfig(Config):
    DEBUG=True
    ENV = 'testing'
    DATABASE_URI= 'postgresql://localhost/reporttest_db'
    TESTING = True

class ProductionConfig(Config):
    DEBUG=True
    ENV = 'testing'
    DATABASE_URI= 'postgres://hoacmgsmjzhvcj:7f9404630082258498e9d5f997e17b4658fd9a496b98e270b98d8ef41685ad47@ec2-54-225-227-125.compute-1.amazonaws.com:5432/d484g16jbnugmf'
    TESTING = False

app_configuration = {
    "development":DevelopmentConfig,
    "testing":TestingConfig,
    "production":ProductionConfig
}

