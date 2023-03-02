from flask import Flask
from flask_mysqldb import MySQL
from config import user, password, database, host

# proximamente implemetacion de corts
app = Flask(__name__)

app.secret_key = 'secret_key'
#creation parameters for connection 
app.config["MYSQL_USER"] = user
app.config["MYSQL_PASSWORD"] = password
app.config["MYSQL_HOST"] = host
app.config["MYSQL_DB"] = database

db = MySQL(app)

#implementation of message handlers
def error_handler(error):
    return '<p>Have you evil inserted the URL? Try again later</p>'

#Blueprint
from routes.login import validate
app.register_blueprint(validate)