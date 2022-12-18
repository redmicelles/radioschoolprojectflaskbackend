import app_config
from config import Config, BASE_DIR
from os import path
from dotenv import load_dotenv

# load environment variables
load_dotenv()

app = app_config.connex_app
app.add_api(path.join(BASE_DIR, "swagger.yaml"))


@app.route("/")
def health_check() -> str:
    return "App Server is running and alive!"


if __name__ == "__main__":
    app.run(host=Config.APP_HOST, port=Config.APP_PORT, debug=Config.APP_DEBUG)
