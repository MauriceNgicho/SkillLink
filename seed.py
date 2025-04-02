from models import storage
from models.course import Course
from models.lesson import Lesson
from models.user import User

# Ensure at least one user exists
user = storage.session.query(User).first()
if not user:
    raise ValueError("No user found in the database. Please create a user first.")

# Delete existing courses
if storage.session.query(Course).first():
    storage.session.query(Course).delete()
    storage.session.commit()

# Create courses
course1 = Course(title="AI and Automation in the Workplace", description="Learn how AI is transforming the modern workplace.", user_id=user.id)
course2 = Course(title="Corporate Ethics and Compliance", description="Understand the fundamentals of corporate ethics.", user_id=user.id)
course3 = Course(title="Customer Service Excellence", description="Enhance your customer service skills.", user_id=user.id)
course4 = Course(title="Digital Marketing Strategies", description="Explore the latest digital marketing techniques.", user_id=user.id)

# Add and commit courses first
storage.session.add_all([course1, course2, course3, course4])
storage.session.commit()

# Create lessons
lesson1 = Lesson(title="Introduction to AI", course_id=course1.id)
lesson2 = Lesson(title="AI in Business Operations", course_id=course1.id)
lesson3 = Lesson(title="Corporate Governance Basics", course_id=course2.id)
lesson4 = Lesson(title="Ethical Decision Making", course_id=course2.id)

# Add and commit lessons
storage.session.add_all([lesson1, lesson2, lesson3, lesson4])
storage.session.commit()

print("Database seeded successfully!")
