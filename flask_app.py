from app import create_app
from config import Config
from os import environ
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.models import sample_model
from app.db import db

app = create_app()

application = app.app
application.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:Password123&!@172.23.0.1:3308/radioschool"
application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(application)
migrate = Migrate(application, db)

# db.init_app(application)
# migrate.init_app(application, db)

@app.route("/")
def health_check():
    return "App Server is running and alive!"

if __name__ == "__main__":
    app.run(host=Config.APP_HOST, port=Config.APP_PORT, debug=Config.APP_DEBUG)