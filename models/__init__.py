"""Initializes the models package"""

from dotenv import load_dotenv
from os import getenv

# Load environment variable from .env file
load_dotenv(override=True)

# Determine storage type
storage_type = getenv("SKILLLINK_STORAGE", "db")

print(f"Storage type selected: {storage_type}")

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    from flask_sqlalchemy import SQLAlchemy

    db = SQLAlchemy()
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    db = None
    storage = FileStorage()

storage.storage_type = storage_type

def init_app(app):
    """Initialize Flask app"""
    if storage_type == "db":
        db.init_app(app)

storage.reload()