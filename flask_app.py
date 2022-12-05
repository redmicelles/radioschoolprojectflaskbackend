from app import create_app
from config import Config
from os import environ
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = create_app()

application = app.app
application.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DATABASE_URI")
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