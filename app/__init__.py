from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config['default'])
    db.init_app(app)

    from app.api.auth import auth_bp
    app.register_blueprint(auth_bp)

    from app.api.manage_user import user_manag_bp
    app.register_blueprint(user_manag_bp)
    
    return app
