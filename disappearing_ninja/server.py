from flask import Flask, render_template, request, redirect, session, flash
import random
import time
import datetime
app = Flask(__name__)
app.secret_key = 'TopSecretMate'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ninja/<int:name>')
def ninja(name):
    return render_template('user.html', name = name)

@app.route('/validate', methods=['POST'])
def validate():
    if len(request.form['fname']) < 1:
        flash("Name is too short!")
    else:
        flash("You shall be known as {}".format(request.form['fname']))
    return redirect('/')

@app.route('/reset')
def reset():
    session['total'] = 0
    session['log'] = []
    return redirect('/')

app.run(debug=True)
