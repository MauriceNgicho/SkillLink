from dotenv import load_dotenv
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from models.user import User
from models.base_model import Base


load_dotenv()

# Initialize database objects
db = SQLAlchemy(model_class=Base)
migrate = Migrate()

def create_app():
    """Factory function to create and configure the Flask app."""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mauricio'
    
    # Configure the database connection
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)  # Bind SQLAlchemy to Flask app
    migrate.init_app(app, db)  # Initialize Flask-Migrate

    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        """Load user from storage by ID."""
        return db.session.get(User, user_id)
    
    @app.context_processor
    def inject_user():
        return dict(user=current_user)

    # Register Blueprints
    from web_flask.routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    from web_flask.routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from web_flask.routes.course import course as course_blueprint
    app.register_blueprint(course_blueprint, url_prefix="/course")



    return app