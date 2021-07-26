import os
from dotenv import load_dotenv

load_dotenv()


def get_int_env(key, default):
    try:
        return int(os.getenv(key))
    except (TypeError, ValueError):
        return default


FLASK_ENV = os.getenv("FLASK_ENV")
FLASK_RUN_HOST = os.getenv("FLASK_RUN_HOST", "localhost")
FLASK_RUN_PORT = get_int_env("FLASK_RUN_PORT", 5678)

POSTGRESQL_URL = os.getenv("POSTGRESQL_URL")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ACCESS_TOKEN_EXPIRES = get_int_env("JWT_ACCESS_TOKEN_EXPIRES", 30)
