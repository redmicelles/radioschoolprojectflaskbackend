
import connexion
from flask_sqlalchemy import SQLAlchemy
import pathlib
from flask_migrate import Migrate


basedir = pathlib.Path(__file__).parent.resolve()

connex_app = connexion.App(__name__, specification_dir=basedir)
app = connex_app.app
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Password123&!@172.23.0.1:3308/radioschool"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
db.init_app(app)

#models should always be import after the SQLAlchemy object initialization
from backend_app.models.access_code_models import AccessCode

migrate = Migrate(app, db)
migrate.init_app(app, db)
