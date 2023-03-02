from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required
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
    return modelUser.get_by_id(db, id)


# routes
@validate.route("/")
def index():
    print("Welcome")
    return redirect(url_for("login.register"))


# register users
@validate.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        respon = modelUser.get_user_exists(db, username) #None

        if respon == None:
            user = User(0,username,password)
            add_user = modelUser.add_user(db, user)

            print (add_user)
            return "In progress Ok"

        else:
            print("user exists already")
            #flash("Insert data...")
            return redirect(url_for("login.login"))

    else:
        return render_template("auth/register.html")


# validation users
@validate.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usermame = request.form["username"]
        password = request.form["password"]
        user = User(0, usermame, password)
        logger_user = modelUser.login(db, user)

        if logger_user != None:  # yes user
            if logger_user.password:  # True password
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


@validate.route("/logout")
def logout():
    logout_user()  # delete seccion user
    return redirect(url_for("login.login"))
