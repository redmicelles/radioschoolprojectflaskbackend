
import connexion
from flask_sqlalchemy import SQLAlchemy
import pathlib
from flask_migrate import Migrate
from log_config import file_handler
from config import BASE_DIR
from flask_cors import CORS
from MySQLdb import OperationalError

connex_app = connexion.App(__name__, specification_dir=BASE_DIR)
app = connex_app.app

#cross origin protection
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

#add log hanler for writing logs to file
app.logger.addHandler(file_handler)

#add SQLAlchemy configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Password123&!@172.23.0.1:3308/radioschool"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
db.init_app(app)

#models should always be import after the SQLAlchemy object initialization
from backend_app.models.access_code_models import AccessCode

migrate = Migrate(app, db)
migrate.init_app(app, db)

# @app.before_request
# def before_request_func():
#     try:
#         db.
#     except Exception as e:
#         return "Errors"
