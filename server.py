from flask import Flask, render_template, session, redirect, request
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)" from emailregex.com
app = Flask(__name__)
mysql = MySQLConnector(app, 'logindb')
# Route to the login/registration page
@app.route('/')
def index():
    return render_template('index.html')

#Route to process the login/registration information
@app.route('/process', methods=['POST'])
def process():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    
    print first_name, last_name, email, password
    return redirect('/success')

# Route to the success/confirmation page
@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True)