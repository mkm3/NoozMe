
from flask import (Flask, render_template, request, flash, session, jsonify,
                   redirect, url_for)

import os

import json

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


@app.route('/api/newsapi/everything', methods=['GET'])
def get_everything():
    """Get everything by keyword."""
    keyword = request.args['keyword']
    res = news.get_everything(keyword)
    return jsonify(res)


@app.route('/api/newsapi/top', methods=['GET'])
def get_top():
    """Get top headlines by category and country."""
    country = request.args['country']
    category = request.args['category']
    res = news.get_top(country=country, category=category)
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
    """Route for handling user login."""
    login = None
    if request.method == 'POST':
        user = db.session.query(User).filter(User.username == request.form['username'], 
                                             User.password == request.form['password']).first()
        
        if user:
            user_id = user.user_id
            session['user_id'] = user_id
            return redirect('/dashboard')
        
        else:
            login = "Invalid credentials"
            
    return render_template('login.html', login=login)


@app.route('/logout', methods=['GET'])
def logout():
    """Route for handling user logout."""
    session.pop('user_id', None)
    return redirect('/login')


@app.route('/save-article', methods=['POST'])
def save_article():
    """Save article to user's profile/saved_news table."""
    title = request.form.get("title")
    image = request.form.get("image")
    description = request.form.get("description")
    content = request.form.get("content")
    pub_date = request.form.get("pub_date")
    url = request.form.get("url")
    
#user_id
#article_id
    
    user = get_logged_in_user()
    crud.save_article(title=title,
                      image=image,
                      description=description,
                      content=content,
                      pub_date=pub_date,
                      news_url=url,
                      user=user)

    return "Article has been saved!"


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
    """Redirect users to dashboard after login or if not logged in."""
    if not is_logged_in():
        return redirect('/login')
    
    user = get_logged_in_user()
    print(f"Successfully logged in as {user.fname} {user.lname}")
    return render_template('dashboard.html', user=user)


@app.route('/api/all-users', methods=['GET'])
def get_all_users():
    """Pull all existing users for typeahead search"""
    all_users = crud.get_all_users()
    return jsonify(all_users)


@app.route('/user/<int:user_id>')
def return_saved_news(user_id):
    """Shows saved news by user_id"""
    user = crud.get_user_by_id(user_id)
    saved_articles = crud.get_saved_news(user)
    return render_template('/profile.html', user=user,
                                            saved_articles=json.dumps(saved_articles))


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
