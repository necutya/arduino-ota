from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from project.config import DevelopmentConfig

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth_bp.login'


def create_app(config_class=DevelopmentConfig):
    # Config application
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize apps
    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)

    from project.auth.routes import auth_bp
    from project.cars.routes import cars_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(cars_bp)

    return db, app
