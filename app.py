from flask import Flask
from flask_mysqldb import MySQL
from routes.cinexrout import cinex
from utils.db import *

app = Flask(__name__)

mysql = MySQL()
app=config(app)
mysql.init_app(app)
app.secret_key ='1234'
app.register_blueprint(cinex)
