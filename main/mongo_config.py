from pymodm import connect

from main.config import DevelopmentConfig


def setup_mongo_connection():
    connect(DevelopmentConfig.DB_URI, alias=DevelopmentConfig.alias)
