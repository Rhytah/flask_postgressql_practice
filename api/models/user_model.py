import datetime
from database.server import DatabaseConnect
from flask import jsonify

db=DatabaseConnect()
class User:
    def __init__(self,args):
        self.username =args['username']
        isadmin=False
        password= None


    def get_users(self):
        cmd = "SELECT * FROM Users;"
        self.cursor.execute(cmd)
        all_users = self.cursor.fetchall()
        return all_users

class Reporter(User):
    def __init__(self):
        super().__init__()

    def create_reporter(self,args):
      add_user_cmd = " INSERT INTO users(userid,firstname,lastname, username, password, email,phone_number,isadmin,registered);"
      self.cursor.execute(add_user_cmd)

        

    def get_reporter(self,user_id):
        cmd= "SELECT * FROM Users WHERE user_id='{}'".format(user_id)
        self.cursor.execute(cmd)
        result=self.cursor.fetchone()
        if result:
            return result
        else:
            return {"message":"User doesn't exist"}

    def search_reporter(self,username,password,email):
        cmd= "SELECT * FROM Users WHERE username='{}',password='{}',email='{}'".format(username,password,email)
        self.cursor.execute(cmd)
        result=self.cursor.fetchone()
        if result:
            return jsonify({"status":400,
            "data": (username,email),
            "message":"User already exists"})