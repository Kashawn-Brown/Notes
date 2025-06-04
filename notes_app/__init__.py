from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from notes_app.config import Config

# Initialize extensions
db = SQLAlchemy()

def create_app(config_class=Config):
    """
    Application factory function that creates and configures
    the Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with app
    db.init_app(app)

    # Import and register blueprints
    from notes_app.routes import notes
    app.register_blueprint(notes.bp)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app 