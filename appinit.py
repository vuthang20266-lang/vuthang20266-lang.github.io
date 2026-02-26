from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # import models sau khi db init
    from appmodels import User

    from approutesauth import auth
    from approutesadmin import admin

    app.register_blueprint(auth)
    app.register_blueprint(admin)

    return app
