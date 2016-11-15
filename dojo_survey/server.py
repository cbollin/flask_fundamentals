from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'TopSecretMate'

@app.route('/')
def index():
    counter = 1
    session['counter'] += counter
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
    print "Got Post Information"
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    # print name, location, language, comment
    return redirect('/show')

app.run(debug=True)
