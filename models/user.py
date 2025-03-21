"""A class user that inherits from BaseModel"""
from models.base_model import BaseModel,Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.exc import IntegrityError
from flask_login import UserMixin
#from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, BaseModel, Base):
    """Represents a user in skillLink."""
    # if getenv("SKILLLINK_STORAGE", "db"):
    # if models.storage.storage_type == 'db':
    if getenv("SKILLLINK_STORAGE") == "db":

        __tablename__ = 'users'
        id = Column(String(60), primary_key=True, nullable=False)
        email = Column(String(128), nullable=False, unique=True)
        password = Column(String(255), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)

        # Relationship: 
        courses = relationship('Course', back_populates='user', cascade='all, delete')
    else:
        id = ""
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize user attributes"""
        if "password" in kwargs:
            self.password = kwargs.pop("password")
        super().__init__(*args, **kwargs)

    def set_password(self, plain_text_password):
        """Hashes and sets the password"""
        self.password = plain_text_password

    def check_password(self, password):
        """Checks if password matches plain text password"""
        return self.password == password
    
    def get_id(self):
        """Return the user ID for session management"""
        return str(self.id)
    
    @classmethod
    def create(cls, email, password, first_name=None, last_name=None):
        """Create a new user with email uniqueness check"""
        from models import storage
        if storage.session.query(User).filter_by(email=email).first():
            raise ValueError("Email is already registered!")

        new_user = cls(email=email, password=password, first_name=first_name, last_name=last_name)

        try:
            storage.new(new_user)
            storage.save()
            return new_user
        except IntegrityError:
            storage.session.rollback()
            raise ValueError("Error saving user. Email might already be taken!")
