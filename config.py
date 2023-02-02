class DevelopmentConfig():
    DEBUG=True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///uniprotinfo.db'
    SECRET_KEY = 'abcabcabcabcabcabc'

config = {
    "development": DevelopmentConfig
}

PREFIX = "/prefix"