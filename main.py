from flask import render_template
from server.wsgi import App
from server.apis import api_blueprint
from server.socket_lib import socketio
import config

app = App().get_app()
app.register_blueprint(api_blueprint)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    socketio.run(app, host=config.FLASK_RUN_HOST, port=config.FLASK_RUN_PORT)
