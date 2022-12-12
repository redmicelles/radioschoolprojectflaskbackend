import os
from dotenv import load_dotenv

#load environment variables
load_dotenv()

#Set App's Base Directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    APP_HOST = os.getenv("APP_HOST") or "0.0.0.0"
    APP_PORT = os.getenv("APP_PORT") or "5000"
    APP_ENV = os.getenv("APP_ENV")
    APP_DEBUG = True if APP_ENV == "development" else False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "123456789"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")

    SQLALCHEMY_TRACK_MODIFICATION = False