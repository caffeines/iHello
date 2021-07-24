import os


def get_int_env(key, default):
    try:
        return int(os.getenv(key), default)
    except (TypeError, ValueError):
        return default


FLASK_ENV = os.getenv("FLASK_ENV")
FLASK_RUN_HOST = os.getenv("FLASK_RUN_HOST", "localhost")
FLASK_RUN_PORT = os.getenv("FLASK_RUN_PORT", 5161)
