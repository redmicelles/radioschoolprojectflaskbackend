import os

# Set App's Base Directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    APP_HOST = os.getenv("APP_HOST") or "0.0.0.0"
    APP_PORT = os.getenv("APP_PORT") or "5000"
    APP_ENV = os.getenv("APP_ENV")
    APP_DEBUG = True if APP_ENV == "development" else False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATION = False

    with open(os.getenv("JWT_PRIVATE_KEY"), "r", encoding="utf8") as pv_key:
        JWT_PRIVATE_KEY = pv_key.read()

    with open(os.getenv("JWT_PRIVATE_KEY"), "r", encoding="utf8") as pbl_key:
        JWT_PUBLIC_KEY = pbl_key.read()
    JWT_AUDIENCE = os.getenv("JWT_AUDIENCE")
    JWT_TTL = int(os.getenv("JWT_TTL"))
    JWT_ISSUER = os.getenv("JWT_ISSUER")
    DATABASE_URI = os.getenv("DATABASE_URI")
