
from flask import (Flask, render_template, request, flash, session, jsonify,
                   redirect, url_for)

import os

from model import db, connect_to_db, User
import crud
import news

from jinja2 import StrictUndefined
import requests


"""Server for movie ratings app."""
app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View homepage."""
    return render_template('homepage.html')


@app.route('/users', methods=['GET'])
def listUsers():
    users = User.query.all()
    serialized_users = []
    for user in users:
        serialized_users.append({
            'fname': user.fname,
            'lname': user.lname,
            'username': user.username,
            'email': user.email
        })
    return jsonify(serialized_users)


@app.route('/api/newsapi', methods=['GET'])
def getTopHeadlines():
    """Get top headlines."""
    keyword = request.args['keyword']
    #change to newsapi.search_by_keyword(keyword)
    res = news.search_by_keyword(keyword)
    return jsonify(res)


def get_logged_in_user():
    """Grabs user information by user_id."""
    user = User.query.get(session['user_id'])
    return user


def is_logged_in():
    """Checks if a user is logged in."""
    if 'user_id' in session:
        return True
    
    else:
        return False
        
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Route for handling the login page logic."""
    login = None
    if request.method == 'POST':
        user = db.session.query(User).filter(User.username == request.form['username'], 
                                             User.password == request.form['password']).first()
        
        if user:
            user_id = user.user_id
            session['user_id'] = user_id
            return redirect('/dashboard')
            # create a session for this logged in user, i.e. add the user to the session
            # Now you can use this session for further interaction with the
            # redirect to their news page        else:
    login = "Invalid credentials"
    return render_template('login.html', login=login)


@app.route('/registration', methods=['GET', 'POST'])
def create_user():
    """Get info from registration."""
    
    if request.method == 'POST':
        crud.create_user(request.form['fname'],
                         request.form['lname'],
                         request.form['email'],
                         request.form['username'],
                         request.form['password'],
                         request.form['zipcode'])
        return redirect('/login')
        
    else:
        flash("Cannot create an account with that email. Try again.")

    return render_template('registration.html')


@app.route('/dashboard', methods=['GET'])
def logged_in():
    """Redirect users to dashboard after login"""
    user = get_logged_in_user()
    print(f"Successfully logged in as {user.fname} {user.lname}")
    return render_template('dashboard.html')


# TRYING TO SHOW SAVED NEWS / PROFILE SETTINGS
# @app.route('/user/<user_id>')
# def show_profile(user_id):
#     """Shows user profile"""
#     user = crud.get_user_by_id(user_id)
#     return render_template('/profile_settings.html', user=user)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
