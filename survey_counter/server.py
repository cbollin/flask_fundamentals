from flask import Flask, render_template, request, redirect, session, flash
import random
import re
import datetime
app = Flask(__name__)
app.secret_key = "TopSecretMate"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route("/")
def index():
    # counter for website counter
    counter = 1
    session["counter"] += counter
    session["someKey"] = 50
    # random number for guessing game
    number = random.randrange(0,101)
    session["number"] = number
    session["guessstatus"] = ""
    return render_template("index.html")

@app.route("/double")
def double():
    counter = 1
    session["counter"] += counter
    return redirect("/")

@app.route("/reset")
def reset():
    session["counter"] = 0
    return redirect("/")

@app.route("/show")
def show_user():
    print "on users page"
    return render_template("user.html")

@app.route("/users", methods=["POST"])
def create_user():
    if len(request.form["name"]) <= 1:
        flash("You must enter a name!")
        return redirect("/")

    elif request.form["name"].isalpha() != True:
        flash("No numbers in your name please!")
        return redirect("/")

    elif len(request.form["password"]) <=1:
        flash("Password too short!")
        return redirect("/")

    elif len(request.form["password"]) >= 8:
        flash("Password is too long")
        return redirect("/")

    elif request.form["password"].isalpha():
        flash("Please use at least 1 number in your password")
        return redirect("/")

    elif request.form["password"].isdigit():
        flash("Please use at least 1 letter in your password")
        return redirect("/")

    elif request.form["password"].islower():
        flash("Please use at least 1 capital letter!")
        return redirect("/")

    elif request.form["password"].isupper():
        flash("Please use at least 1 lower case letter!")
        return redirect("/")

    elif request.form["password_confirm"] != request.form["password"]:
        flash("Passwords must match")
        return redirect("/")

    elif len(request.form["comment"]) <= 1:
        flash("Comment field is too short!")
        return redirect("/")

    elif len(request.form["comment"]) >= 250:
        flash("Comment field too long, try again!")
        return redirect("/")

    elif len(request.form["email"]) <= 1:
        flash("Email field is too short!")
        return redirect("/")

    elif not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid email")
        return redirect("/")

    else:
        session["name"] = request.form["name"]
        session["password"] = request.form["password"]
        session["location"] = request.form["location"]
        session["language"] = request.form["language"]
        session["comment"] = request.form["comment"]
        session["email"] = request.form["email"]
        flash("Success")
    return redirect("/show")

# guessing game route
@app.route("/takeguess", methods=["POST"])
def take_guess():
    guess = int(request.form["guess"])
    number = session["number"]
    if guess == number:
        print "correct"
        session["guessstatus"] = "correct"
    elif guess < number:
        print "too low"
        session["guessstatus"] = "too low"
    elif guess > number:
        print "too high"
        session["guessstatus"] = "too high"
    return render_template("/index.html")
app.run(debug=True)
