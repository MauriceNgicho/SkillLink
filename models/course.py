"""A class Course that inherits from BaseModel"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Course(BaseModel, Base):
    """Represents a course in skillLink."""

    if getenv("SKILLLINK_STORAGE") == "db":
        __tablename__ = 'courses'
        id = Column(String(60), primary_key=True, nullable=False)
        title = Column(String(128), nullable=False)
        description = Column(String(255), nullable=True)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

        # Relationship: A course belongs to a user and has many lessons
        lessons = relationship('Lesson', backref='course', cascade='all, delete')

    else:
        id = ""
        title = ""
        description = ""
        user_id = ""

    def __init__(self, *args, **kwargs):
        """Initialize Course attributes"""
        super().__init__(*args, **kwargs)

    #def add_lesson(self, lesson_id):
     #   """Adds a lesson to the course"""
      #  if lesson_id not in self.lesson_ids:
       #     self.lesson_ids.append(lesson_id)