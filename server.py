"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, url_for)
from model import connect_to_db
import crud
from newsapi import NewsApiClient
import os
from jinja2 import StrictUndefined

NEWS_API_KEY = os.environ.get('API_KEY')
newsapi = NewsApiClient(api_key=os.environ.get('API_KEY'))

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

#put inside a function
url = "https://newsapi.org/v2/everything?q=bats&apiKey=" + NEWS_API_KEY
response = request.get(url)
response_json =  response.json()
pprint.pprint(response_json)

#everything = https://newsapi.org/v2/everything?q=bitcoin&apiKey=YOURAPIKEY

# @app.route('/')
# def homepage():
#     """View homepage."""

#     return render_template('homepage.html')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     """Route for handling the login page logic."""
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             return redirect(url_for('home'))
#     return render_template('login.html', error=error)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
