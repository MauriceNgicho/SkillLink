from dotenv import load_dotenv
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
import pymysql
from sqlalchemy.orm import scoped_session, sessionmaker
from models.user import User
from models.course import Course
from models.lesson import Lesson

pymysql.install_as_MySQLdb()

load_dotenv()

classes = {
    "BaseModel": BaseModel,
    "Course": Course,
    "User": User,
    "Lesson": Lesson
}


class DBStorage:
    """Handles database interactions using SQLAlchemy for MariaDB"""

    __engine = None
    __session = None


    def __init__(self):
        """Initialize db connection using environment variables."""


        db_user = getenv("SKILLLINK_MYSQL_USER")
        db_password = getenv("SKILLLINK_MYSQL_PWD")
        db_host = getenv("SKILLLINK_MYSQL_HOST")
        db_name = getenv("SKILLLINK_MYSQL_DB")

        self.__engine = create_engine(
            f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
            pool_pre_ping=True
        )

        if getenv("SKILLLINK_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        """Create session and bind it to engine."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def new(self, obj):
        """Adds new object to session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commits all changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from session"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def all(self, cls=None):
        """Retrieve all objects from the database"""
        obj_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = f"{obj.__class__.__name__}.{obj.id}"
                obj_dict[key] = obj
        else:
            for model in classes.values():
                objs = self.__session.query(model).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    obj_dict[key] = obj
        return (obj_dict)
    
    def get(self,cls,id):
        """Retrieve an obj by class and ID."""
        if cls not in classes.values():
            return None
        if isinstance(id, str) and id.isdigit():
            return self.__session.query(cls).get(id)
        if cls == User:  # Allow searching by email for Users
            return self.__session.query(User).filter_by(email=id).first()
        return None
    
    def close(self):
        """Close the session"""
        self.__session.remove()

    @property
    def session(self):
        """Expose the session"""
        return self.__session
        

        
