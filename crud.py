"""CRUD Operations."""

import os
import re
from model import db, User, Article, Saved, Subscription, Category, Country, connect_to_db

from sqlalchemy.exc import IntegrityError

from datetime import datetime

def create_user(fname, lname, email, username, password, category, country):
    """Create and return a new user."""
    try:
        user = User(fname=fname,
                    lname=lname,
                    email=email,
                    username=username,
                    password=password,
                    preferred_category_id=category,
                    preferred_country_id=country)

        db.session.add(user)
        db.session.commit()
        return user

    except IntegrityError:
        db.session.rollback()
        return None

def get_user_by_id(user_id):
    """Return a user by primary key"""
    return User.query.get(user_id)


def get_article_by_id(article_id):
    """Return a user by primary key"""
    return Article.query.get(article_id)


def save_article(title,image,description,content,pub_date,news_url,user):
    """Save an article to your profile."""
    article = Article(title=title,
                    image=image,
                    description=description,
                    content = content,
                    pub_date=datetime.strptime(pub_date, "%Y-%m-%dT%H:%M:%SZ"),
                    news_url=news_url
                    )
    
    db.session.add(article)
    
    #testing
    print(article)
    
    # 2.0 add rating and notes during save event
    #creating the relationship between user and the saved article
    saved_article = Saved(user=user,
                          article=article)
                        #   notes=notes,
                        #   rating=rating)
    
    db.session.add(saved_article)
    db.session.commit()

    #testing
    print(saved_article)
    

def save_subscribed_article(user_id, article_id):
    """Logged in user can save article that is under another user's saved_news feed."""
    user = User.query.get(user_id)
    article = Article.query.get(article_id)
    
    saved_article = Saved(user=user, article=article)
    
    db.session.add(saved_article)
    db.session.commit()

    return True

def get_saved_news(user, origin="saved"):
    """Grab saved news by user."""
    
    saved_news_feed = []
    
    for entry in user.saved_news:
        article = entry.article
        print(article.article_id)
        article_item = {
            "title" : article.title,
            "image" : article.image,
            "description" : article.description,
            "content" : article.content,
            "pub_date" : article.pub_date.strftime("%m/%d/%Y"),
            "news_url" : article.news_url,
            "saved_news_id" : entry.id,
            "origin" : origin,
            "article_id" : article.article_id
        }
        saved_news_feed.append(article_item)
    print(saved_news_feed)
    return saved_news_feed     


def get_all_users():
    """Pull all existing users for typeahead search."""
    all_users = User.query.all()
    
    list_of_all_users = []
    for user in all_users:
        list_of_all_users.append({
            'user_id' : user.user_id,
            'username' : user.username,
            'fname' : user.fname,
            'lname' : user.lname,
            'total_articles' : len(user.saved_news)
            })
        
    return list_of_all_users


def get_category_entries():
    """Pull all category_entries."""
    category_entries = Category.query.all()
    return category_entries


def get_country_entries():
    """Pull all country_entries."""
    country_entries = Country.query.all()
    return country_entries


def remove_saved_article(user_id, saved_news_id,):
    """Remove saved article under user profile."""
    article_to_remove = Saved.query.filter(Saved.user_id == user_id and Saved.id == saved_news_id).first()

    if article_to_remove:
        db.session.delete(article_to_remove)
        db.session.commit()
        return True
    return False

#TODO 2.0                      
def subscribe(user_id, profile_user_id):
    """Follow another user."""
    user = get_user_by_id(user_id)
    #profile of other user
    subscribe_to = get_user_by_id(profile_user_id)

    subscription = Subscription(user=user, 
                                subscribe_to=subscribe_to)

    db.session.add(subscription)
    db.session.commit()


#TODO 2.0
def unsubscribe(user_id, profile_user_id):
    """Unfollow another user."""
    subscription = Subscription.query.filter(
        Subscription.user_id == user_id and 
        Subscription.subscribe_to == profile_user_id
        ).first()

    db.session.delete(subscription)
    db.session.commit()


def is_subscribed(user_id, profile_user_id):
    """Check if user is subscribed to another user."""

    subscription = Subscription.query.filter(
        Subscription.user_id == user_id and 
        Subscription.subscribe_to == profile_user_id
        ).first()
    print(subscription)
    return subscription is not None


#TODO
def update_user(user_id, email, preferred_category_id, preferred_country_id):
    """Updates user settings (category and country)."""
    user = User.query.get(user_id)

    user.email = email
    user.preferred_category_id = preferred_category_id
    user.preferred_country_id = preferred_country_id

    db.session.commit()
    return user
    

#TODO NTH
def rate_article():
    """Update article rating."""
    pass


#TODO NTH
def add_note():
    """Add a note to an article."""
    pass


#TODO NTH
def add_profile_photo():
    """Upload photo to user profile"""
    pass