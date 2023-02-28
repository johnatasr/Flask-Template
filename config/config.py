import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # This only for representation always put sensitive data in envs
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY', "fkk38477jjmmx55178jedtk")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        "mysql+pymysql://root:v25xhycLlRY3sV7Z@localhost:3306/exercise"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
