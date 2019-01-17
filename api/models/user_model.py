import datetime
from database.server import DatabaseConnect
from flask import jsonify

db=DatabaseConnect()
class User:
    def __init__(self):
        # self.username =args['username']
        isadmin=False
        password= None


    def get_users(self):
        cmd = "SELECT * FROM Users;"
        db.cursor.execute(cmd)
        all_users = db.cursor.fetchall()
        return all_users

class Reporter(User):
    def __init__(self):
        super().__init__()

    def create_reporter(self,userid,firstname,lastname, username, password, email,phone_number,isadmin,registered):
      add_user_cmd = " INSERT INTO users(userid,firstname,lastname, username, password, email,phone_number,isadmin,registered) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(firstname,lastname, username, password, email,phone_number,isadmin,registered)
      db.cursor.execute(add_user_cmd)

        

    def get_reporter(self,userid):
        cmd= "SELECT * FROM Users WHERE userid='{}'".format(userid)
        db.cursor.execute(cmd)
        result=db.cursor.fetchone()
        if result:
            return result
        else:
            return {"message":"User doesn't exist"}

    def search_reporter(self,email):
        cmd= "SELECT * FROM Users WHERE email='{}'".format(email)
        db.cursor.execute(cmd)
        result=db.cursor.fetchone()
        if result:
            return jsonify({"status":400,
            "data": (email),
            "message":"User already exists"})