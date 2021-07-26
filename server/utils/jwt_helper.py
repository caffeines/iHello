import config
from server.wsgi import App
from flask_jwt_extended import create_access_token, JWTManager
import datetime

app = App().get_app()
app.config["JWT_SECRET_KEY"] = config.JWT_SECRET_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(
    days=config.JWT_ACCESS_TOKEN_EXPIRES
)
jwt_manager = JWTManager(app)


def create_jwt(user_id: str, user_type="public"):
    additional_claims = {"aud": user_type}
    token = create_access_token(identity=user_id, additional_claims=additional_claims)
    return token
