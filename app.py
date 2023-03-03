from flask import Flask, redirect, url_for
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
#from flask_cors import CORS

from config import user, password, database, host

app = Flask(__name__)
csrf = CSRFProtect()

#CORS(app,resources={r"/api/*": {"origins": "http://0.0.0.0"}})

app.secret_key = 'secret_key'
#creation parameters for connection 
app.config["MYSQL_USER"] = user
app.config["MYSQL_PASSWORD"] = password
app.config["MYSQL_HOST"] = host
app.config["MYSQL_DB"] = database

db = MySQL(app)

#implementation of message handlers
def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return '<p>website not found</p>',404

#Blueprint
from routes.login import validate
app.register_blueprint(validate)