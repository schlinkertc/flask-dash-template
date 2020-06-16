
"""Flask config."""
from os import environ, path
from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname('flask-dash-template'))
load_dotenv(path.join(BASE_DIR, '.env'))

class Config:
    """Flask configuration variables."""
    

    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = 'wsgi.py'
    FLASK_ENV = 'development'

    # Assets
    LESS_BIN = path.join(BASE_DIR,'node_modules/.bin/lessc')
    ASSETS_DEBUG = True
    ASSETS_AUTO_BUILD = True

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')
    
    #SQLAlchemy
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False