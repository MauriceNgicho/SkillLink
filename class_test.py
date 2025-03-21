from models import storage
from models.user import User
from models.course import Course
from models.lesson import Lesson

# Create a User
user1 = User(email="test@example.com", password="securepass", first_name="John", last_name="Doe")
print(user1)  # Check if User object initializes correctly

# Create a Course
course1 = Course(title="Python Basics", description="Learn Python from scratch", instructor_id=user1.id)
print(course1)  # Check Course initialization

# Create a Lesson
lesson1 = Lesson(title="Introduction to Python", content="Python basics content", course_id=course1.id)
print(lesson1)  # Check Lesson initialization

# Add a resource to the lesson
# lesson1.add_resource("https://docs.python.org/3/")
# print(lesson1.resources)  # Check if resource is added correctly

# Add to storage
storage.new(user1)
storage.new(course1)
storage.new(lesson1)
storage.save()

print("objects saved successfully!")