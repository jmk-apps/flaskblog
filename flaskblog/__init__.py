from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config


class Base(DeclarativeBase):
    pass


login_manager = LoginManager()
db = SQLAlchemy(model_class=Base)
mail = Mail()

# If a user tries to access a route (i.e one that has login_required) without loging in, they are redirected to the login route.
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"

from flaskblog.models import User, Post


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    with app.app_context():
        db.create_all()

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
