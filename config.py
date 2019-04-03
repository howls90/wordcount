class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    DEBUG = True
    TABLE_NAME='WordCountProduction',
    REGION_NAME = 'us-west-2', 
    ENPOINT_URL = "http://dynamodb:8000", 
    AWS_ACCESS_KEY_ID = 'xxx', 
    AWS_SECRET_ACCESS_KEY = 'xxx',
    ERROR_404_HELP = False

class DevelopmentConfig(Config):
    DEBUG = True
    TABLE_NAME='WordCountDevelopment',
    REGION_NAME = 'us-west-2', 
    ENPOINT_URL = "http://dynamodb:8000", 
    AWS_ACCESS_KEY_ID = 'xxx', 
    AWS_SECRET_ACCESS_KEY = 'xxx',
    ERROR_404_HELP = True

class TestingConfig(Config):
    TESTING = True
    TABLE_NAME='WordCountTesting',
    REGION_NAME = 'us-west-2', 
    ENPOINT_URL = "http://dynamodb:8000", 
    AWS_ACCESS_KEY_ID = 'xxx', 
    AWS_SECRET_ACCESS_KEY = 'xxx',
    ERROR_404_HELP = False
