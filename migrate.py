import os
from flask import Flask
from models import db, init_app, storage
from models.user import User
from models.course import Course

# Set up Flask app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///skilllink.db")  # Adjust as needed
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize database
init_app(app)

# Run Alembic migrations
print("Generating new migration...")
os.system("alembic revision --autogenerate -m 'Auto-migration update'")

print("Applying migrations...")
os.system("alembic upgrade head")

print("Migration completed successfully!")

# ✅ Add Application Context for Querying the Database
with app.app_context():
    user = User.query.first()  # Get the first user if available

    if user:
        if not Course.query.filter_by(title="Python for Beginners").first():
            course1 = Course(title="Python for Beginners", description="Learn Python from scratch.", user_id=user.id)
            course2 = Course(title="Flask Web Development", description="Build web apps using Flask.", user_id=user.id)

            db.session.add_all([course1, course2])
            db.session.commit()

            print("✅ Sample courses added successfully!")
        else:
            print("✅ Sample courses already exist. Skipping data insertion.")
    else:
        print("⚠️ No users found! Please create a user first.")
