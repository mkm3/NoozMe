"""CRUD Operations."""

from model import db, User, Article, Saved, Friendship, Preference, Topic, News_Topic, User_Interest, connect_to_db

def create_user(fname, lname, email, username, password):
    """Create and return a new user."""

    user = User(fname=fname,
                lname=lname,
                email=email,
                username=username,
                password=password)

    db.session.add(user)
    db.session.commit()

    return user

def save_article():
    """Save an article to your profile."""
    pass


def follow_person():
    """Follow another user."""
    pass