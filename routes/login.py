from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager ,login_user, logout_user, login_required
from app import db, app

# models
from models.modelUser import modelUser

# evtiti
from models.intities.user import User

# blueprint
validate = Blueprint("login", __name__)

login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return modelUser.get_by_id(db,id)

# routes
@validate.route("/")
def index():
    print("Welcome")
    return redirect(url_for("login.login"))


@validate.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usermame = request.form["username"]
        password = request.form["password"]
        user = User(0, usermame, password)
        logger_user = modelUser.login(db, user)

        if logger_user != None:  #yes user
            if logger_user.password: #True password
                login_user(logger_user)
                return redirect(url_for("login.home"))
            else:
                flash("Invalid password..")
                return render_template("auth/login.html")
        else:
            flash("User not found..")
            return render_template("auth/login.html")
    else:
        return render_template("auth/login.html")


@validate.route("/home")
def home():
    return render_template("home.html")
