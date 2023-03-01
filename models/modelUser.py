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

    @classmethod
    def get_user_exists(self, db,username):
        try:
           cursor = db.connection.cursor()
           sql = "SELECT * FROM login WHERE username = '{}'".format(username)
           cursor.execute(sql)
           new = cursor.fetchone()

           if new != None:
            return new
           else:
            return None  
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_user(self,db, user):
        try:
            cursor = db.connection.cursor()   
            sql = "INSERT INTO login(username, password) VALUES('{}','{}')".format(user.username, user.password)
            cursor.execute(sql)
            cursor.close()

            return True          
        except Exception as ex:
            raise Exception(ex)