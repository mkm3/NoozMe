
from logging import LoggerAdapter
import profile
from flask import (Flask, render_template, request, flash, session, jsonify,
                   redirect, url_for)
from sqlalchemy.exc import IntegrityError

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
    """Load web app."""
    return redirect('/login')


@app.route('/api/newsapi/everything', methods=['GET'])
def get_everything():
    """Get everything by keyword."""
    keyword = request.args['keyword']
    res = news.get_everything(keyword)
    return jsonify(res)


@app.route('/api/newsapi/top', methods=['GET'])
def get_top():
    """Get top headlines by category and country."""

    user = get_logged_in_user()
    country = user.preferred_country.country_value
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
    if is_logged_in():
        return redirect('/dashboard')
    
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
    note = request.form.get("note")

    
    user = get_logged_in_user()
    crud.save_article(
        title=title,
        image=image,
        description=description,
        content=content,
        pub_date=pub_date,
        news_url=url,
        note=note,
        user=user)

    return "Article has been saved!"


@app.route('/save-subscribed-article', methods=['POST'])
def save_another_users_saved_article():
    """Save article from another user's saved news."""    
    user = get_logged_in_user()
    user_id = user.user_id
    
    article_id = request.form.get("article_id")
    crud.save_subscribed_article(user_id, article_id)

    return "You saved their article!"


@app.route('/remove-article', methods=['POST'])
def remove_article():
    """Removed article from database"""
    saved_news_id = request.form.get("saved_new_id")
    user_id = get_logged_in_user().user_id
    
    if crud.remove_saved_article(
        saved_news_id=saved_news_id,
        user_id=user_id):
        return 'Saved article has been removed!'
    return 'Sorry, error occurred.'

@app.route('/registration', methods=['GET', 'POST'])
def create_user():
    """Get info from registration."""
    
    categories = crud.get_category_entries()
    countries = crud.get_country_entries()

    if request.method == 'POST':
        user = crud.create_user(
            #['string'] = the "name" field within the form
            request.form['fname'],
            request.form['lname'],
            request.form['email'],
            request.form['username'],
            request.form['password'],
            request.form['category_id'],
            request.form['country_id'])
        if user:
            #testing
            print("User has been created!")
            return redirect('/login')
        else:
            flash("User exists. Please try again.")


    return render_template(
        'registration.html',
        categories=categories,
        countries=countries
        )


@app.route('/dashboard', methods=['GET'])
def get_dashboard():
    """Redirect users to dashboard after login or if not logged in."""
    if not is_logged_in():
        return redirect('/login')
    
    logged_in_user = get_logged_in_user()

    subscriptions_list = crud.get_subsciptions_by_user(logged_in_user.user_id)

    print(f"Successfully logged in as {logged_in_user.fname} {logged_in_user.lname}")
    return render_template(
        'dashboard.html', 
        logged_in_user=logged_in_user,
        subscriptions_list=subscriptions_list
    )

#TODO
@app.route('/settings', methods=['GET','POST'])
def get_or_update_settings():
    """Redirects users to Settings from dashboard and pulls category and country preferences saved"""
    
    categories = crud.get_category_entries()
    countries = crud.get_country_entries()

    user = get_logged_in_user()
    if request.method == 'POST':
        new_email = request.form['email']
        new_category_pref = request.form['category_id']
        new_country_pref = request.form['country_id']
        user = crud.update_user(
            user_id=user.user_id, 
            email=new_email, 
            preferred_category_id=new_category_pref, 
            preferred_country_id=new_country_pref)
    
    return render_template(
        'settings.html',
        logged_in_user=user,
        categories=categories,
        countries=countries
        )


@app.route('/api/all-users', methods=['GET'])
def get_all_users():
    """Pull all existing users for typeahead search"""
    all_users = crud.get_all_users()
    return jsonify(all_users)


@app.route('/user/<int:profile_id>')
def return_profile(profile_id):
    """Redirect to user profile (login user and other users)."""
    if not is_logged_in():
        return redirect('/login')
    
    logged_in_user = get_logged_in_user()
    user = crud.get_user_by_id(profile_id)
                            
                            #expression to evaluate T or F
    is_not_logged_in_user = user.user_id != logged_in_user.user_id
    
    if logged_in_user == user:
        saved_articles = crud.get_saved_news(user)
    else:       
        saved_articles = crud.get_saved_news(user, "subscription")
    
    print("Check Subscription " + str(profile_id))
    is_subscribed = crud.is_subscribed(logged_in_user.user_id, profile_id)
    subscriptions_list = crud.get_subsciptions_by_user(profile_id)

    return render_template('/profile.html', user=user,
                                            saved_articles=json.dumps(saved_articles),
                                            logged_in_user=logged_in_user,
                                            is_not_logged_in_user=is_not_logged_in_user,
                                            is_subscribed=is_subscribed,
                                            subscriptions_list=subscriptions_list)


@app.route('/api/toggle-subscribe', methods=['POST'])
def toggle_subscribe():
    """Subscribe and unsubscribe to other users."""

    #logged in user
    if not is_logged_in():
        return "Error occurred because user is not logged in."

    user = get_logged_in_user()

    #other user's profile user id
    profile_user_id = request.form['profile_user_id']
    user_id = user.user_id

    if crud.is_subscribed(user_id, profile_user_id):
        crud.unsubscribe(user_id, profile_user_id)
        return "You've unsubscribed!"
    
    crud.subscribe(user.user_id, profile_user_id)

    return "You made a new subscription!"

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

