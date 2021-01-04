from flaskext.mysql import MySQL
from flask import Flask, render_template, request

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'eu-cdbr-west-03.cleardb.net'
app.config['MYSQL_DATABASE_USER'] = 'be2cab09e7c0ae'
app.config['MYSQL_DATABASE_PASSWORD'] = '7bc7c902'
app.config['MYSQL_DATABASE_DB'] = 'heroku_34d7acf27b26d39'

mysql.init_app(app)
conn = mysql.connect()
cursor =conn.cursor()

#query functions
def queryTest():
    cursor.execute("SELECT * FROM items")
    data = cursor.fetchall()
    return data