from flask_socketio import SocketIO
from ..wsgi import App
import eventlet

eventlet.monkey_patch()

app = App().get_app()
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")
