#Flask-SQLAlchemy configuration I
from os import environ, path
basedir = path.abspath(path.dirname(__file__))

from dotenv import load_dotenv
load_dotenv(path.join(basedir, '.env'))


#Flask-SQLAlchemy configuration II
class Config:

    """Set Flask configuration from .env file."""
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
    SERVER_NAME = environ.get('SERVER_NAME')

    SQLALCHEMY_DATABASE_URI = "{db_type}+{db_connector}://{username}:{password}@{hostname}/{databasename}".format(
        db_type=environ.get('DB_TYPE'),
        db_connector=environ.get('DB_CONNECTOR'),
        username=environ.get('USERNAME'),
        password=environ.get('SECRET_KEY'),
        hostname=environ.get('HOST'),
        databasename=environ.get('DB_NAME')
    )
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_RECYCLE = 290
    DEBUG = False

    # Configuration
    GOOGLE_CLIENT_ID = environ.get("GOOGLE_CLIENT_ID", None)
    GOOGLE_CLIENT_SECRET = environ.get("GOOGLE_CLIENT_SECRET", None)
    GOOGLE_DISCOVERY_URL = environ.get('GOOGLE_DISCOVERY_URL')


    # Flask-Assets
    #LESS_BIN = environ.get('LESS_BIN')
    #ASSETS_DEBUG = environ.get('ASSETS_DEBUG')
    #LESS_RUN_IN_DEBUG = environ.get('LESS_RUN_IN_DEBUG')

    # Compile static assets
    #if app.config['FLASK_ENV'] == 'development':
    #compile_assets(app)

    # Static Assets
    #STATIC_FOLDER = 'static'
    #TEMPLATES_FOLDER = 'templates'
    #COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')

