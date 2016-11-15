from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'TopSecretMate'

@app.route('/')
def index():
    # counter for website counter
    counter = 1
    session['counter'] += counter
    session['someKey'] = 50
    # random number for guessing game
    number = random.randrange(0,101)
    session['number'] = number
    session['guessstatus'] = ''
    print number
    return render_template('index.html')

@app.route('/double')
def double():
    counter = 1
    session['counter'] += counter
    return redirect('/')

@app.route('/reset')
def reset():
    session['counter'] = 0
    return redirect('/')

@app.route('/show')
def show_user():
    return render_template('user.html')

@app.route('/users', methods=['POST'])
def create_user():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/show')

# guessing game route
@app.route('/takeguess', methods=['POST'])
def take_guess():
    guess = int(request.form['guess'])
    number = session['number']
    if guess == number:
        print 'correct'
        session['guessstatus'] = 'correct'
    elif guess < number:
        print 'too low'
        session['guessstatus'] = 'too low'
    elif guess > number:
        print 'too high'
        session['guessstatus'] = 'too high'
    return render_template('/index.html')
app.run(debug=True)
