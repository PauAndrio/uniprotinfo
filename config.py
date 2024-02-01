import random
import string


class DevelopmentConfig():
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///uniprotinfo.db'
    SECRET_KEY = 'abcabcabcabcabcabc'


class ProducctionConfig():
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///uniprotinfo.db'
    SECRET_KEY = ''.join(random.choices(string.ascii_letters, k=30))


config = {
    "development": DevelopmentConfig,
    "producction": ProducctionConfig
}

# IMPORTANT PREFIX should start with an slash ("/") character
PREFIX = "/uniprotinfo"
