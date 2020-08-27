"""CRUD Operations."""

import os
from model import db, User, Article, Saved, Follower, Preference, Topic, News_Topic, User_Interest, connect_to_db


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

def get_user_by_id(user_id):
    """Return a user by primary key"""
    return User.query.get(user_id)


def save_article(title,image,description,content,pub_date,news_url,user_id,article_id,):
    """Save an article to your profile."""
    article = Article(title=title,
                    image=image,
                    description=description,
                    content = content,
                    pub_date=pub_date,
                    news_url=news_url
                    )
    
    
    db.session.add(article)
    db.session.commit()
    
    print(article)
    
    # 2.0 add rating and notes during save event
    saved_article = Saved(user_id=user_id,
                          article_id=article_id)
                        #   notes=notes,
                        #   rating=rating)
    
    db.session.add(saved_article)
    db.session.commit()

    print(saved_article)

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