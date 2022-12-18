from config import BASE_DIR
from os import path
from logging import FileHandler, config, Formatter, INFO, DEBUG, basicConfig

config.dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)
FORMAT = "%(asctime)s : %(levelname)s : %(name)s : %(message)s"
file_handler = FileHandler(path.join(BASE_DIR, f"app_logs/applogs.log"))
file_handler.setFormatter(Formatter(FORMAT))
file_handler.setLevel(DEBUG)
