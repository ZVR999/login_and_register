from flask import Flask, render_template, session, redirect, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'logindb')
# Route to the login/registration page
@app.route('/')
def index():
    return render_template('index.html')

# Route to the success/confirmation page
@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True)