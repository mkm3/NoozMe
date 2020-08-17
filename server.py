
from flask import (Flask, render_template, request, flash, session, jsonify,
                   redirect, url_for)
from newsapi import NewsApiClient

from model import db, connect_to_db, User
import crud

import os
from jinja2 import StrictUndefined
import requests


"""Server for movie ratings app."""
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
newsapi = NewsApiClient(api_key=os.environ.get('NEWS_API_KEY'))

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


@app.route('/top-headlines', methods=['GET'])
def getTopHeadlines():
    url = "https://newsapi.org/v2/everything?q=bats&apiKey=" + NEWS_API_KEY
    response = request.get(url)
    response_json =  response.json()
    return response_json


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Route for handling the login page logic."""
    error = None
    if request.method == 'POST':
        print("MADE IT TO POST")
        print(request.form)
        user = db.session.query(User).filter(User.username == request.form['username'], 
                                             User.password == request.form['password']).first()
        
        if user:
            pass
            # create a session for this logged in user, i.e. add the user to the session
            # Now you can use this session for further interaction with the
            # redirect to their news page
            # error = f"Successfully Logged In as {user.fname} {user.lname}" <-- this is just for debugging purposes
        else:
            error = "Invalid credentials"
    return render_template('login.html', error=error)



@app.route('/registration', methods=['GET', 'POST'])
def createUser():
    pass




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
