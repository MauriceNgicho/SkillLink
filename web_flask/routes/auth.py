from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import storage
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,logout_user, login_required, current_user
from web_flask.forms import LoginForm, SignUpForm
from models.user import User


auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["Get", "POST"])
def login():
    form = LoginForm()

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Query user by email
        user = storage.session.query(User).filter_by(email=email).first()

        #if user and user.password == password:
        if user and check_password_hash(user.password_hash, password):
            login_user(user, remember=True)
            flash("Login successful!", "success")
            return redirect(url_for("main.home"))
        else:
            flash("Invalid email or password", category="error")

    return render_template("login.html", user=current_user, form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully", category="info")
    return redirect(url_for("auth.login"))

@auth.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    """Handles user registration"""
    form = SignUpForm()
    if form.validate_on_submit():
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        password = form.password.data
        #confirm_password = request.form.get("confirm_password")
        confirm_password = form.confirm_password.data

        # Query user by email to check if already exists
        existing_user = storage.session.query(User).filter_by(email=email).first()
        if existing_user:
            flash("Email already exists. Please log in.", category="error")
            return redirect(url_for("auth.sign_up"))
        elif password != confirm_password:
            flash("Passwords do not match.", category="error")
        else:
            hashed_password = generate_password_hash(password)
            new_user = User(email=email, first_name=first_name, last_name=last_name, password_hash=hashed_password)

            storage.new(new_user)
            storage.save()
            login_user(new_user) # Auto-login after signup
            flash("Account created!", category="success")
            return redirect(url_for("main.home"))

    return render_template("sign_up.html", user=current_user, form=form)