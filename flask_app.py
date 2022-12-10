import app_config
from config import Config

app = app_config.connex_app
app.add_api(app_config.basedir / "swagger.yaml")

@app.route("/")
def health_check():
    return "App Server is running and alive!"

if __name__ == "__main__":
    app.run(host=Config.APP_HOST, port=Config.APP_PORT, debug=Config.APP_DEBUG)