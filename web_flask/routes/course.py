from flask import Blueprint, render_template

course = Blueprint("course", __name__)

@course.route("/courses")
def list_courses():
    return render_template("courses.html")