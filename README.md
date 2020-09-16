# NoozMe :newspaper:	

## About
NoozMe creates a succinct and organized version of news sharing that ties in a subscriber element to the experience. NoozMe lets the user browse articles quickly while also allowing them to build a mini-museum of saved articles that other users can view. The inspiration for my project stems from my passion with journalism and keeping up with current events. In a day an age where anyone can share an article without any context, NoozMe serves as a perfect solution to tailormade and customize that experience!

## API
[News API](https://newsapi.org/)

## Tech Stack 
* Python 
* Flask
* PostgreSQL
* SQLAlchemy
* JavaScript 
* jQuery
* HTML
* Jinja
* CSS
* Bootstrap

## Features 
* MVP 1 - Customized Filters
    * Ability to use a customized search to retrieve news articles (NewsAPI request)
        * By Category
        * By Country

* MVP 2 - Save Button 
    * Ability to save content under personal login (or session) 
        * User can be redirected to a new page to find all their saved content
        * User can add article description/comment during the saving process

* MVP 3 - Search Engine 
    * Ability to do a keyword search to find new content (NewsAPI request)
  
* MVP 4 - Social Aspect
    * Ability to do a search and subscribe to other user's profiles
        * User can find users by first name, last name and username
        * User can add other users to their subscription list by clicking "subscribe"

## Installation

### Virtual Environment
Create a virtual environment to install requirements

```sh
$ virtualenv
$ source env/bin/activate
```

### Prerequisites
All the prerequisites are in the requirements.txt file 

```sh
pip3 install -r requirements.txt
```

### Run Server 

```sh
python3 server.py
```



## Using NoozMe
### 1. Register as a new user or login to your account
![](https://github.com/mkm3/NoozMe/blob/master/static/assets/gifs/register.gif "Register or Login")

### 2. Browse Articles
![](https://github.com/mkm3/NoozMe/blob/master/static/assets/gifs/browse.gif "Browse Articles")

### 3. Save articles to your Noozeum


### 4. Search for other users


### 5. Explore and subscribe to other users Noozeums!


## Author 
Michelle Macaraeg
**[LinkedIn](https://www.linkedin.com/in/macaraegm/)**
**[GitHub](https://github.com/mkm3)**


## Acknowledgments
* *Hackbright Instructors:* Marisa Gloor, Katrina Huber-Juma, Andrew Blum

**Thank you all for your support and guidance throughout the program!**