from flask import render_template

from app.auth import auth


@auth.route('/signup', methods=["GET", "POST"])
def signup():
    return render_template('forms/signup.html')


@auth.route('/login', methods=["GET", "POST"])
def login():
    return render_template('forms/login.html')
