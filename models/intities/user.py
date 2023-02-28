# structructure for table login  => "regsiter users"
from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, username, password, fullname=""):
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname

    @classmethod
    def check_password(self, hash_password, password):
        return check_password_hash(hash_password, password)

#print(generate_password_hash('password'))