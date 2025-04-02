"""
Contains class BaseModel
"""


from datetime import datetime
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

time_format = "%Y-%m-%dT%H:%M:%S.%f"

if models.storage_type == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """The Base class for all future classes"""
    if models.storage_type == "db":
        id = Column(String(60), primary_key=True, unique=True, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
        updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            
            # Conert string dates back to datetime
            if "created_at" in kwargs and isinstance(self.created_at, str):
                self.created_at = datetime.strptime(kwargs["created_at"], time_format)
            else:
                self.created_at = datetime.utcnow()
            
            if "updated_at" in kwargs and isinstance(self.updated_at, str):
                self.updated_at = datetime.strptime(kwargs["updated_at"], time_format)
            else:
                self.updated_at = datetime.utcnow()

            if "id" not in kwargs:
                self.id = str(uuid.uuid4())

        else:

            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
    
    def save(self):
        """Update 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into key/values dictionary format"""
        new_dict = self.__dict__.copy()

        #convert datetime attributes to string format
        if "created_at" in new_dict:
            new_dict["created_at"] = self.created_at.isoformat()
        if "updated_at" in new_dict:
            new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        if "__sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        
        return new_dict
    
    def __str__(self):
        """String representation of BaseModel class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def delete(self):
        """dlete the current instance from storage"""
        models.stroge.delete(self)
