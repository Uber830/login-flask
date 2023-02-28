# data for the connection to the database server
from dotenv import load_dotenv
import os

load_dotenv()
#class DevelopmentConfig():
user = os.environ['MYSQL_USER'] 
password = os.environ['MYSQL_PASSWORD']
host = os.environ['MYSQL_HOST']
database = os.environ['MYSQL_DB'] 