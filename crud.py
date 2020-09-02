"""CRUD Operations."""

import os
from model import db, User, Article, Saved, Subscription, Preference, Topic, News_Topic, User_Interest, connect_to_db
from datetime import datetime

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


def get_saved_news(user):
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
            "news_url" : article.news_url
        }
        saved_news_feed.append(article_item)
    print(saved_news_feed)
    return saved_news_feed     


def get_all_users():
    """Pull all existing users for typeahead search"""
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
        

#TODO 2.0                      
def subscribe():
    """Follow another user."""
    pass


#TODO 2.0
def unsubscribe():
    """Unfollow another user."""
    pass


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