import psycopg2 
from flask import current_app as app
from config import app_configuration


class DatabaseConnect:
    def __init__(self):
        self.connection_credentials = dict(
            dbname = '',
            user = 'postgres',
            host = 'localhost'
        )
        self.conn =psycopg2.connect(dbname="", user="postgres", host="localhost")
        self.cursor=self.conn.cursor()
        self.conn.autocommit = True
        
    # def connectdb(self):
        if app.config.get('ENV') == 'development':
            dbname = app_configuration['development'].DATABASE
            self.connection_credentials['dbname'] = dbname
           

        if app.config.get('ENV') == 'testing':
            dbname = app_configuration['testing'].DATABASE
            self.connection_credentials['dbname'] = dbname
           
        try:
            self.conn = psycopg2(**self.connection_credentials)
            self.conn.autocommit = True
            self.cursor = self.conn.cursor()

            print(f"You have connected to {dbname}")
        except:
            print("connection failed")

        usercmd="CREATE TABLE IF NOT EXISTS users(user_id SERIAL PRIMARY KEY,firstname,lastname,username VARCHAR (30),password VARCHAR (10),email VARCHAR (30),phone_number INT,isadmin BOOLEAN DEFAULT FALSE NOT NULL,registered)"
        self.cursor.execute(usercmd)
    
        redflagsql="CREATE TABLE IF NOT EXISTS redflags(redflag_id SERIAL PRIMARY KEY,created_by VARCHAR(20),incident_type DEFAULT REDFLAG NOT NULL,location INT, status VARCHAR(15),image,video,comment VARCHAR (225))"
        self.cursor.execute(redflagsql)
    
        interventionsql="CREATE TABLE IF NOT EXISTS redflags(redflag_id SERIAL PRIMARY KEY,created_by VARCHAR(20),incident_type DEFAULT INTERVENTION NOT NULL,location INT, status VARCHAR(15),image,video,comment VARCHAR (225))"
        self.cursor.execute(interventionsql)
        adminuser=f"""
                INSERT INTO users(username, password, role)
                VALUES('admin','admin' ,TRUE)
                """
        self.cursor.execute(adminuser)

    def drop_table(self,tablename):
        command = f"""
        DROP TABLE IF EXISTS {tablename} CASCADE
        """
        return self.cursor.execute(command)