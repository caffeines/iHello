from wsgi import App
from flask_sqlalchemy import SQLAlchemy
import config


class Config(object):
    SQLALCHEMY_DATABASE_URI = config.POSTGRESQL_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = App().get_app()
app.config.from_object(Config)
db = SQLAlchemy(app)
