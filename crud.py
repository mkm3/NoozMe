"""CRUD Operations."""

import os
from model import db, User, Article, Saved, Follower, Preference, Topic, News_Topic, User_Interest, connect_to_db
from newsapi import NewsApiClient

NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
newsapi = NewsApiClient(api_key=os.environ.get('NEWS_API_KEY'))


def create_user(fname, lname, email, username, password, zipcode):
    """Create and return a new user."""

    user = User(fname=fname,
                lname=lname,
                email=email,
                username=username,
                password=password,
                zipcode=zipcode)

    db.session.add(user)
    db.session.commit()

    return user

def login():
    """User login and session"""
    pass

#move to newsapi.py
def search_by_keyword(keyword):
    """Search article by keyword search engine."""
    top_headlines = newsapi.get_top_headlines(q=keyword)
    return top_headlines


def search_by_custom_fields():
    """Search article by custom fields."""
    pass


def save_article():
    """Save an article to your profile."""
    pass


'''
MVP 1,2,3 - Finish Line
'''


def follow_user():
    """Follow another user."""
    pass


def unfollow_user():
    """Unfollow another user."""
    pass


def update_zipcode():
    """Update location settings from homepage or profile settings."""
    pass


def rate_article():
    """Update article rating."""
    pass


def add_note():
    """Add a note to an article."""
    pass


def logout():
    """Logout user."""
    pass