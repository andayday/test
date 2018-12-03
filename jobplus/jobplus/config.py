class BaseConfig(object):
    SECRET_KEY = 'this is a test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/jobplus?charset=utf8'

class ProductConfig(BaseConfig):
    pass

class TestConfig(BaseConfig):
    pass 


configs = {
        'development': DevelopmentConfig,
        'product': ProductConfig,
        'test': TestConfig,
        }


