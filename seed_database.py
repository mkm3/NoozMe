"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
from model import *
import server

os.system('dropdb noozme_db')
os.system('createdb noozme_db')

connect_to_db(server.app)
db.create_all()

#Test users
user1 = User(fname="Max", lname="Murphy", email="mrm@gmail.com", username="murphdog777", password="password123", zipcode = 94596, language="en")
user2 = User(fname="Michelle", lname="Macaraeg", email="mkm@gmail.com", username="mikkster3", password="password123", zipcode = 94596, language="en")
user3 = User(fname="Robbie", lname="Macaraeg", email="ram@gmail.com", username="robizamac", password="password123", zipcode = 94596, language="en")
user4 = User(fname="Charlie", lname="Bear", email="ruff@gmail.com", username="pumpkinhead", password="password123", zipcode = 94596, language="en")
user5 = User(fname="Hadley", lname="Kitten", email="meow@gmail.com", username="snuggles", password="password123", zipcode = 94596, language="en")

users = [user1, user2, user3, user4, user5]
db.session.add_all(users)

#Test articles
article1 = Article(title = "Test Article 1", image = "blah", description = "test description", pub_date = datetime.now(), news_url = "blahURL")
article2 = Article(title = "Test Article 2", image = "blah", description = "test description", pub_date = datetime.now(), news_url = "blahURL")
article3 = Article(title = "Test Article 3", image = "blah", description = "test description", pub_date = datetime.now(), news_url = "blahURL")
article4 = Article(title = "Test Article 4", image = "blah", description = "test description", pub_date = datetime.now(), news_url = "blahURL")
article5 = Article(title = "Test Article 5", image = "blah", description = "test description", pub_date = datetime.now(), news_url = "blahURL")

articles = [article1, article2, article3, article4, article5]
db.session.add_all(articles)

#Test saves_news
saved1 = Saved(user = user1, article = article1, notes="great read", rating = 5)
saved2 = Saved(user = user3, article = article2, notes="well written", rating = 4)
saved3 = Saved(user = user2, article = article4, notes="hardly credible", rating = 1)
saved4 = Saved(user = user3, article = article4, notes="horrible", rating = 1)
saved5 = Saved(user = user4, article = article1, notes="fantastic article", rating = 5)
saved6 = Saved(user = user5, article = article5, notes="surprising read", rating = 4)

saved_list = [saved1, saved2, saved3, saved4, saved5, saved6]
db.session.add_all(saved_list)

db.session.commit()

# with open('data/articles.json') as f:
#     article_data = json.loads(f.read())
    
# print(article_data)

# # Create movies, store them in list so we can use them
# # to create fake ratings
# movies_in_db = []
# for movie in movie_data:
#     title, overview, poster_path = (movie['title'],
#                                     movie['overview'],
#                                     movie['poster_path'])
#     release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

#     db_movie = crud.create_movie(title,
#                                  overview,
#                                  release_date,
#                                  poster_path)
#     movies_in_db.append(db_movie)

# # Create 10 users; each user will make 10 ratings
# for n in range(10):
#     email = f'user{n}@test.com'  # Voila! A unique email!
#     password = 'test'

#     user = crud.create_user(email, password)

#     for _ in range(10):
#         random_movie = choice(movies_in_db)
#         score = randint(1, 5)

#         crud.create_rating(user, random_movie, score)
