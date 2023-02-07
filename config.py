import random, string

class DevelopmentConfig():
    DEBUG=True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///uniprotinfo.db'
    SECRET_KEY = 'abcabcabcabcabcabc'

class ProducctionConfig():
    DEBUG=False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///uniprotinfo.db'
    SECRET_KEY = ''.join(random.choices(string.ascii_letters, k=30))

config = {
    "development": DevelopmentConfig,
    "producction": ProducctionConfig
}

PREFIX = "/uniprotinfo"