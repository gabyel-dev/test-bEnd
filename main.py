from flask import Flask
from config import Config
from flask_cors import CORS
from controllers.auth import auth_bp
from utils.hash_password import bcrypt
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)
jwt = JWTManager(app)


CORS(app, supports_credentials=True)
bcrypt.init_app(app)

app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)