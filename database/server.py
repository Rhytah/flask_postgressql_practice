import psycopg2 
from flask import current_app as app
from config import app_configuration
from psycopg2.extras import RealDictCursor
import os

class DatabaseConnect:
    def __init__(self):
        self.connection_credentials = """
        dbname='report_db' user='postgres' host='localhost' password='mine' port='5432'
        """
        self.conn =psycopg2.connect(self.connection_credentials)
        self.cursor=self.conn.cursor()
        self.conn.autocommit = True

        try:
            self.connection_credentials1= """
                dbname = "d484g16jbnugmf" host = "ec2-54-225-227-125.compute-1.amazonaws.com" password ="7f9404630082258498e9d5f997e17b4658fd9a496b98e270b98d8ef41685ad47"
                user = "hoacmgsmjzhvcj"

            """
                
            if app.config.get('ENV') == 'development':
                
                dbname = app_configuration['development'].DATABASE_URI
                self.connection_credentials['dbname'] = dbname
                self.conn.autocommit = True
                self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)
                self.conn = psycopg2.connect(self.connection_credentials)
                print("\n\n Database Connected\n\n")

            if app.config.get('ENV') == 'testing':
                dbname = app_configuration['testing'].DATABASE_URI
                self.connection_credentials['dbname'] = dbname
                self.conn.autocommit = True
                self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)
                self.conn = psycopg2.connect(self.connection_credentials)
                print("\n\n Database Connected\n\n")

            if app.config.get('ENV') == 'production':
              
                self.conn.autocommit = True
                self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)
                self.conn = psycopg2.connect(self.connection_credentials1)
                print("\n\n Database Connected\n\n")
        except:
            print("connection failed")


        usercmd="""CREATE TABLE IF NOT EXISTS users(
            user_id SERIAL PRIMARY KEY,
            firstname VARCHAR (30),
            lastname VARCHAR (30),
            username VARCHAR (30),
            password VARCHAR (10),
            email VARCHAR (30),
            phone_number INT,
            isadmin BOOLEAN DEFAULT FALSE NOT NULL,
            registered TIMESTAMP DEFAULT NOW())"""
        self.cursor.execute(usercmd)
    
        redflagsql="""CREATE TABLE IF NOT EXISTS redflags(
            redflag_id SERIAL PRIMARY KEY,
            created_by VARCHAR(20),
            incident_type VARCHAR (30) NOT NULL,
            location INT, 
            status VARCHAR(15),
            comment VARCHAR (225))"""
        self.cursor.execute(redflagsql)
    
        interventionsql="""CREATE TABLE IF NOT EXISTS interventions(
            intervention_id SERIAL PRIMARY KEY,
            created_by VARCHAR(20),
            incident_type VARCHAR (30) NOT NULL,
            location INT, 
            status VARCHAR(15),
            comment VARCHAR (225))"""
        self.cursor.execute(interventionsql)
        adminuser=f"""
                INSERT INTO users(username, password, isadmin)
                VALUES('admin','admin' ,TRUE)
                """
        self.cursor.execute(adminuser)

    def drop_table(self,tablename):
        command = f"""
        DROP TABLE IF EXISTS {tablename} CASCADE
        """
        return self.cursor.execute(command)