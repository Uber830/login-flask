from models.intities.user import User

class modelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """select * from login where username = '{}'""".format(user.username)
            cursor.execute(sql)
            new = cursor.fetchone()

            if new != None:
                user = User(new[0], new[1], User.check_password(new[2],user.password),new[3])
                return user
            else:
              return None  
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """select id, username, fullname  from login where id = {}""".format(id)
            cursor.execute(sql)
            new = cursor.fetchone()

            if new != None:
                return User(new[0], new[1],None,new[2])
            else:
              return None  
        except Exception as ex:
            raise Exception(ex)