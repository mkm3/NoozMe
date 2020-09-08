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



#Test categories
category1 = Category(category_value="business", category_string="Business")
category2 = Category(category_value="entertainment", category_string="Entertainment")
category3 = Category(category_value="general", category_string="General")
category4 = Category(category_value="health", category_string="Health")
category5 = Category(category_value="science", category_string="Science")
category6 = Category(category_value="sports", category_string="Sports")
category7 = Category(category_value="technology", category_string="Technology")

categories = [category1, category2, category3, category4, category5, category6]
db.session.add_all(categories)


#Test countries
country_codes = ["ar", "au", "at", "be", "br", "bg", "ca", "cn", "co",
                "cu", "cz", "eg", "fr", "de", "gr", "hk", "hu", "in",
                "id", "ie", "il", "it", "jp", "lv", "lt", "my", "mx",
                "ma", "nl", "nz", "ng", "no", "ph", "pl", "pt", "ro",
                "ru", "sa", "rs", "sg", "sk", "si", "za", "kr", "se",
                "ch", "tw", "th", "tr", "ae", "ua", "gb", "us", "ve"]

countries = ["Argentina", "Australia", "Austria", "Belgium", "Brazil", 
            "Bulgaria", "Canada", "China", "Columbia", "Cuba", "Czech Republic", 
            "Eqypt", "France", "Germany", "Greece", "Hong Kong", "Hungary", 
            "India", "Indonesia", "Ireland", "Israel", "Italy", "Japan", "Latvia", 
            "Lithuania", "Malaysia", "Mexico", "Morocco", "Netherlands", "New Zealand", 
            "Nigeria", "Norway", "Philippines", "Poland", "Portugal", "Romania", "Russia", 
            "Saudi Arabia", "Serbia", "Singapore", "Slovakia", "Slovenia", "South Africa", 
            "South Korea", "Sweden", "Switzerland", "Taiwan", "Thailand", "Turkey", "UAE", "Ukraine", 
            "United Kingdom", "United States", "Venuzuela"]

country_entries = []

for country_code, country in zip(country_codes, countries):
    country_entries.append(Country(country_value=country_code, country_string=country))

db.session.add_all(country_entries)

#Phrase for ratings (i.e. "<User.fname> thought this article was <phrase>.")
phrases = ["adorable","bad","baffling","concise","crazy","credible","critical","cute","delightful",
            "disgraceful","dispicable","excellent","exciting","fake","fantastic","fascinating",
            "happy","helpful","horribly written","horrifying","informative","insightful","inspiring",
            "interesting","motivating","mysterious","not credible","poorly written","quirky","ridiculous",
            "sarcastic","satirical","shocking","silly","sinical","stupid","suprising","suspicious",
            "well written","wonderful"]


#Test users
user1 = User(fname="Max", lname="Murphy", email="mrm@gmail.com", username="murphdog777", password="password123", preferred_category_id=1, preferred_country_id=1)
user2 = User(fname="Michelle", lname="Macaraeg", email="mkm@gmail.com", username="mikkster3", password="password123", preferred_category_id=1, preferred_country_id=1)
user3 = User(fname="Robbie", lname="Macaraeg", email="ram@gmail.com", username="robizamac6", password="password123", preferred_category_id=1, preferred_country_id=1)
user4 = User(fname="Charlie", lname="Bear", email="ruff@gmail.com", username="pumpkinhead12", password="password123", preferred_category_id=1, preferred_country_id=1)
user5 = User(fname="Hadley", lname="Kitten", email="meow@gmail.com", username="snuggles8", password="password123", preferred_category_id=1, preferred_country_id=1)

users = [user1, user2, user3, user4, user5]
db.session.add_all(users)

#Test articles
article1 = Article(title = "Test Article 1", image = "blah", description = "test description", content = "test content", pub_date = datetime.now(), news_url = "blahURL")
article2 = Article(title = "Test Article 2", image = "blah", description = "test description", content = "test content", pub_date = datetime.now(), news_url = "blahURL")
article3 = Article(title = "Test Article 3", image = "blah", description = "test description", content = "test content", pub_date = datetime.now(), news_url = "blahURL")
article4 = Article(title = "Test Article 4", image = "blah", description = "test description", content = "test content", pub_date = datetime.now(), news_url = "blahURL")
article5 = Article(title = "Test Article 5", image = "blah", description = "test description", content = "test content", pub_date = datetime.now(), news_url = "blahURL")

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

#Test subscriptions
subscription1 = Subscription(user=user1, subscribe_to=user2, created=datetime.now())
subscription2 = Subscription(user=user2, subscribe_to=user3, created=datetime.now())
subscription3 = Subscription(user=user3, subscribe_to=user4, created=datetime.now())
subscription4 = Subscription(user=user4, subscribe_to=user5, created=datetime.now())
subscription5 = Subscription(user=user5, subscribe_to=user1, created=datetime.now())

subscriptions = [subscription1, subscription2, subscription3, subscription4, subscription5]
db.session.add_all(subscriptions)


#commit all tests to database tables
db.session.commit()
