SkillLink
🚀 A corporate e-learning platform built with Flask, SQLAlchemy, and Alembic.

📌 About the Project
SkillLink is a corporate e-learning platform that enables companies to manage training programs, track progress, and facilitate knowledge sharing among employees.

This project is being developed as an MVP (Minimum Viable Product) with Flask, SQLAlchemy, and Alembic for database migrations. It includes support for both file-based (FileStorage) and database (DBStorage) storage.

✨ Features
✅ User authentication (login/signup)
✅ Course management (CRUD operations for courses)
✅ User progress tracking
✅ Support for multiple storage backends (JSON & SQLAlchemy)
✅ Admin dashboard (Future feature)

🛠️ Tech Stack
Backend: Flask, Flask-SQLAlchemy, Alembic
Frontend: HTML, CSS, JavaScript (Vanilla & jQuery)
Database: SQLite (default), PostgreSQL (planned for production)
Storage Options: JSON-based file storage & SQLAlchemy database storage
📂 Project Structure
bash
Copy code
SkillLink/
│── models/                 # Data models (SQLAlchemy ORM & JSON storage)
│   ├── engine/             # Storage engines (FileStorage & DBStorage)
│   ├── user.py             # User model
│   ├── course.py           # Course model
│   ├── __init__.py         # Storage initialization
│── migrations/             # Alembic migrations
│── templates/              # HTML templates
│── static/                 # CSS, JS, and images
│── auth.py                 # Authentication logic
│── app.py                  # Main Flask application
│── migrate.py              # Database migration script
│── .env                    # Environment variables
│── requirements.txt        # Python dependencies
│── README.md               # Project documentation


Contact
📌 Maurice Ngicho
💼 Software Engineer | Full-Stack Developer
📧 mrcngicho@gmail.com
🔗 MauriceNgicho


