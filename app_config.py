import connexion
from flask_sqlalchemy import SQLAlchemy
import pathlib
from flask_migrate import Migrate
from log_config import file_handler
from config import BASE_DIR
from flask_cors import CORS
from config import Config
import traceback
import sys

# from MySQLdb import OperationalError

connex_app = connexion.App(__name__, specification_dir=BASE_DIR)
app = connex_app.app

# cross origin protection
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# add log hanler for writing logs to file
app.logger.addHandler(file_handler)

# add SQLAlchemy configuration
app.config["SQLALCHEMY_DATABASE_URI"] = Config.DATABASE_URI
print(Config.DATABASE_URI)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
db.init_app(app)

# models should always be import after the SQLAlchemy object initialization
from backend_app.models.access_code_models import AccessCode
from backend_app.api_errors import SpecialErrors

migrate = Migrate(app, db)
migrate.init_app(app, db)

# Generic error handler
from flask import json
from werkzeug.exceptions import HTTPException


@app.errorhandler(404)
def page_not_found(e):
    app.logger.error(e)
    return SpecialErrors.error_404, 404


@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return e
    app.logger.error(e, exc_info=sys.exc_info())
    # exc_type, exc_value, exc_tb = sys.exc_info()
    # app.logger.error(traceback.TracebackException(exc_type, exc_value, exc_tb))
    return SpecialErrors.error_500, 500
