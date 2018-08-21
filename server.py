from flask import Flask, render_template, session, redirect, request, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)" from emailregex.com
app = Flask(__name__)
app.secret_key = '12n1!c@$Tdcapunc2$Tcasch52r828'
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
    confirm_password = request.form['confirm_password']
    # First Name validation
    if len(first_name) < 2:
        flash('First Name must be longer than 2 characters')
        return redirect('/')
    elif not first_name.isalpha():
        flash('First Name must not contain any numbers')
        return redirect('/')
    # Last Name validation
    if len(last_name) < 2:
        flash('Last Name must be longer than 2 characters')
        return redirect('/')
    elif not last_name.isalpha():
        flash('Last Name must not contain any numbers')
        return redirect('/')
    # Email validation
    if not EMAIL_REGEX.match(email):
        flash('Email is not in a vaild format')
        return redirect('/')
    #Password validation
    if len(password) < 8:
        flash('Password must be atleast 8 characters')
        return redirect ('/')
    #Confirm Password validation
    if confirm_password != password:
        flash('Password and Confirm Password do not match')
        return redirect('/')
    print first_name, last_name, email, password
    return redirect('/success')

# Route to the success/confirmation page
@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True)