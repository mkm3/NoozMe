import os
# import requests
import json

#Script to help run News output more quickly
import pycurl
from io import BytesIO

from urllib.parse import urlencode, quote_plus

NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

#Script to help run News output more quickly
def get_json_url(url):
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.IPRESOLVE, pycurl.IPRESOLVE_V4)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    value = buffer.getvalue()
    res = json.loads(value)
    return res


def convert_json(api_articles):
    
    articles = []
    
    for article in api_articles:
        my_article = {
            'title' : article['title'],
            'image' : article['urlToImage'],
            'description' : article['description'],
            'content' : article['content'],
            'pub_date' : article['publishedAt'],
            'news_url' : article['url'],
            'origin' : 'newsapi'
        }
        articles.append(my_article)
        
    return articles


#TODO limit results
def get_top(country="", category=""):
    """converts json response - for category and country endpoint"""
    url = f"http://newsapi.org/v2/top-headlines?apiKey={NEWS_API_KEY}"
    
    if country:
        url = url + f"&country={country}"
    if category:
        url = url + f"&category={category}"

    # res = requests.get(url)
    # api_articles = res.json()['articles']

    api_articles = get_json_url(url)['articles']
    
    articles = convert_json(api_articles)
    return articles


#TODO limit results
def get_everything(keyword):
    """converts json response - for everything endpoint"""
    url = 'http://newsapi.org/v2/everything?'

    payload = {
        "language" : "en",
        "q" : keyword,
        "apiKey" : NEWS_API_KEY
    }

    url_encoded_payload = urlencode(payload, quote_via=quote_plus)
    url = url + url_encoded_payload

    api_articles = get_json_url(url)['articles']
        
    articles = convert_json(api_articles)
    
    return articles