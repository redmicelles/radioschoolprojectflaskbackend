
import connexion
from flask_sqlalchemy import SQLAlchemy
import pathlib
from flask_migrate import Migrate
from config import Config
from ma import ma

basedir = pathlib.Path(__file__).parent.resolve()

connex_app = connexion.App(__name__, specification_dir=basedir)
app = connex_app.app
app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
db.init_app(app)
ma.init_app(app)

#models should always be import after the SQLAlchemy object initialization
from backend_app.models.access_code_models import AccessCode

migrate = Migrate(app, db)
migrate.init_app(app, db)