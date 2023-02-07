class DevelopmentConfig():
    DEBUG=True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///uniprotinfo.db'
    SECRET_KEY = 'abcabcabcabcabcabc'

class ProducctionConfig():
    DEBUG=False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///uniprotinfo.db'
    SECRET_KEY = 'asldkfjcqwlekrjwoiqwn'

config = {
    "development": DevelopmentConfig,
    "producction": ProducctionConfig
}

PREFIX = "uniprotinfo"