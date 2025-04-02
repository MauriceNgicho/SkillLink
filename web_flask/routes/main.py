from flask import Blueprint, render_template
from models import storage
from models.course import Course

main = Blueprint("main", __name__)

@main.route("/")
def home():
    courses = storage.session.query(Course).limit(4).all()
    return render_template("home.html", courses=courses)