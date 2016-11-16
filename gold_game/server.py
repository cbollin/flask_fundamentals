from flask import Flask, render_template, request, redirect, session, flash
import random
import time
import datetime
app = Flask(__name__)
app.secret_key = 'TopSecretMate'

@app.route('/')
def index():
    if 'log' not in session:
        session['log'] = []
    if 'total' not in session:
        session['total'] = 0
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    if request.form['building'] == 'farm':
        session['name'] = 'farm'
        session['gold'] = random.randrange(10,21)

    elif request.form['building'] == 'casino':
        session['name'] = 'casino'
        session['gold'] = random.randrange(-50, 51)

    elif request.form['building'] == 'cave':
        session['name'] = 'cave'
        session['gold'] = random.randrange(5, 11)

    elif request.form['building'] == 'house':
        session['name'] = 'house'
        session['gold'] = random.randrange(2, 6)

    # time stuff
    ts = s = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    session['total'] += session['gold']
    session['log'].append("You earned {} gold from the {} at {}".format(session['gold'], session['name'], st))
    session['log'].reverse()

    return redirect('/')

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
