import connexion
from os import path
from config import (
    Config,
    BASE_DIR
)


def create_app(config_class=Config):

    app = connexion.App(__name__, specification_dir="./")
    app.add_api(path.join(BASE_DIR, "swagger.yaml"))

    # db.init_app(app)
    # Migrate(app, db)

    return app