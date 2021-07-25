from server.wsgi import App
from server.apis import api_blueprint
import config

app = App().get_app()
app.register_blueprint(api_blueprint)


if __name__ == "__main__":
    app.run(host=config.FLASK_RUN_HOST, port=config.FLASK_RUN_PORT)
