import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '6575fae36288be6d1bad40b99808e37f')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    AUDIO_FILE_PATH = "../static/audio.wav"
    DB_URI = 'mongodb://localhost:27017/FirstSource'
    alias = "FirstSource"


config_by_name = dict(
    dev=DevelopmentConfig
)
key = Config.SECRET_KEY
