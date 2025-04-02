"""A class Lesson that inherits from BaseModel"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Lesson(BaseModel, Base):
    """Represents a lesson in SkillLink."""
    
    if getenv("SKILLLINK_STORAGE") == "db":
        __tablename__ = 'lessons'
        id = Column(String(60), primary_key=True, nullable=False)
        title = Column(String(128), nullable=False)
        content = Column(String(5000), nullable=True)
        course_id = Column(String(60), ForeignKey('courses.id'), nullable=False)

    
    else:
        id = ""
        title = ""
        content = ""
        course_id = ""

    def __init__(self, *args, **kwargs):
        """Initialize Lesson attributes"""
        super().__init__(*args, **kwargs)