
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


@app.route('/', methods=['GET', 'POST'])
def index():
    search = MusicSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('homepage.html', form=search)

# @app.route("/")
# def root():
#     return render_template('root.html')

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
    keyword = request.args['keyword']
    #change to newsapi.search_by_keyword(keyword)
    res = news.search_by_keyword(keyword)
    return jsonify(res)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Route for handling the login page logic."""
    login = None
    if request.method == 'POST':
        user = db.session.query(User).filter(User.username == request.form['username'], 
                                             User.password == request.form['password']).first()
        
        if user:
            pass
            # create a session for this logged in user, i.e. add the user to the session
            # Now you can use this session for further interaction with the
            # redirect to their news page
            # error = f"Successfully Logged In as {user.fname} {user.lname}" <-- this is just for debugging purposes
        else:
            login = "Invalid credentials"
    return render_template('registration.html', login=login)



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
        flash('Cannot create an account with that email. Try again.')

    return render_template("registration.html")


# TRYING TO SHOW SAVED NEWS / PROFILE SETTINGS
# @app.route('/user/<user_id>')
# def show_profile(user_id):
#     """Shows user profile"""
#     user = crud.get_user_by_id(user_id)
#     return render_template('/profile_settings.html', user=user)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
