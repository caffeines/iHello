from wsgi import App
import config

app = App().get_app()


@app.route("/")
def index():
    return {"message": "ok"}


if __name__ == "__main__":
    app.run(host=config.FLASK_RUN_HOST, port=config.FLASK_RUN_PORT)
