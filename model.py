"""Models for NoozMe app."""

from datetime import datetime
from email.policy import default
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, 
                        autoincrement=True, 
                        primary_key=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable= False)
    email = db.Column(db.String, nullable=False, unique=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    zipcode = db.Column(db.Integer, nullable=False)
    # language = db.Column(db.String)
    last_updated = db.Column(db.DateTime)
    created = db.Column(db.DateTime)

    def __repr__(self):
        return f'<User user_id={self.user_id} fname={self.fname} lname={self.lname} username={self.username}>'


class Article(db.Model):
    """A article."""

    __tablename__ = 'articles'

    article_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    title = db.Column(db.String)
    image = db.Column(db.String)
    description = db.Column(db.String)
    content = db.Column(db.String)
    pub_date = db.Column(db.DateTime)
    news_url = db.Column(db.String)

    def __repr__(self):
        return f'<Article article_id={self.article_id} description={self.description} pub_date={self.pub_date} news_url={self.news_url}>'


class Saved(db.Model):
    """A saved article."""

    __tablename__ = 'saved_news'

    id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    article_id = db.Column(db.Integer, db.ForeignKey('articles.article_id'))
    notes = db.Column(db.String)
    rating = db.Column(db.Integer)
    
    user = db.relationship('User', backref='saved_news')
    article = db.relationship('Article', backref='saved_news')

    def __repr__(self):
        return f'<Saved id={self.id} user_id={self.user_id} article_id={self.article_id} notes={self.notes} rating={self.rating}>'


class Subscription(db.Model):
    """A subscription connection."""

    __tablename__ = 'subscriptions'

    id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    subscribe_to_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    created = db.Column(db.DateTime, default=datetime.now())
    
    user = db.relationship('User', primaryjoin = user_id == User.user_id)
    subscribe_to = db.relationship('User', primaryjoin = subscribe_to_id == User.user_id)

    def __repr__(self):
        return f'<Subscription id={self.id} user={self.user} subscribe_to={self.subscribe_to} created={self.created}>'
    


class Preference(db.Model):
    """A user preference tied to language and zipcode."""

    __tablename__ = 'user_preferences'

    id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    language = db.Column(db.String)
    zipcode = db.Column(db.Integer)
    
    user = db.relationship('User', backref='user_preferences')

    def __repr__(self):
        return f'<Preference id={self.id} user_id={self.user_id} language={self.language} zipcode={self.zipcode}>'
    

class Topic(db.Model):
    """A topic of interest (i.e. Technology, Finance)."""

    __tablename__ = 'topics'

    id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    topic = db.Column(db.String)

    def __repr__(self):
        return f'<Topic id={self.id} topic={self.topic}>'
    
    
class News_Topic(db.Model):
    """A topic of interest (i.e. Technology, Finance)."""

    __tablename__ = 'news_topics'

    id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('articles.article_id'))
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    
    article = db.relationship('Article', backref='news_topics')
    topic = db.relationship('Topic', backref='news_topics')

    def __repr__(self):
        return f'<News_Topic id={self.id} article_id={self.article_id} topic_id={self.topic_id}>'
    
    
class User_Interest(db.Model):
    """A topic of interest (i.e. Technology, Finance)."""

    __tablename__ = 'user_interests'

    id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    
    user = db.relationship('User', backref='user_interests')
    topic = db.relationship('Topic', backref='user_interests')

    def __repr__(self):
        return f'<News_Topic id={self.id} article_id={self.article_id} topic_id={self.topic_id}>'
    
    
def connect_to_db(flask_app, db_uri='postgresql:///noozme_db', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
