from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = 'secret key 1'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'loginreg_asp')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def create():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    password = request.form['password']
    email = request.form['email']
    # run validations and if they are successful we can create the password hash with bcrypt
    pw_hash = bcrypt.generate_password_hash(password)
    # now we insert the new user into the database
    insert_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
    query_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': pw_hash
    }
    mysql.query_db(insert_query, query_data)
    # redirect to success page
    return redirect('/success')

@app.route('/login', methods=['POST'])
def login():
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = { 'email': request.form['email'] }
    user = mysql.query_db(user_query, query_data) # user will be returned in a list
    if bcrypt.check_password_hash(user[0]['password'], request.form['password']):
    # login user
        session['user'] = user[0]
        return redirect('/success')
    else:
    # set flash error message and redirect to login page
        flash('Error')
        return redirect('/')

@app.route('/success')
def success():
    query = "SELECT * FROM users" # define your query
    users = mysql.query_db(query) # run query with query_db()
    return render_template('results.html', users=users) # pass data to our template

app.run(debug=True)
