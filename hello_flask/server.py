from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', phrase='kittens', times=5)

@app.route('/kittens')
def kittens():
    return render_template('kittens.html')

@app.route('/forms')
def kittenforms():
    return render_template('kittenforms.html')

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Information"
    name = request.form['name']
    email = request.form['email']
    print name, email
    return redirect('/')

app.run(debug=True)
