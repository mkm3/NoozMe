import os
import requests

NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

def get_everything(keyword):
    url = ( 'http://newsapi.org/v2/everything?' +
            'language=en' +
            '&q=' + keyword +
            '&apiKey=' + NEWS_API_KEY)
    print(url)
    res = requests.get(url)
    return res.json()


def test_get_everything(keyword):
    url = ( 'http://newsapi.org/v2/everything?' +
            'language=en' +
            '&q=' + keyword +
            '&apiKey=' + NEWS_API_KEY)
    print(url)
    res = requests.get(url)
    newsapi_articles = res.json()['articles']
    
    articles = []
    
    for article in newsapi_articles:
        my_article = {
            'title' : article['title'],
            'image' : article['urlToImage'],
            'description' : article['description'],
            'content' : article['content'],
            'pub_date' : article['publishedAt'],
            'news_url' : article['url']
        }
        articles.append(my_article)
        print(articles)
        return articles


def get_sources():
    pass


def get_top(country="", category=""):
    url = f"http://newsapi.org/v2/top-headlines?apiKey={NEWS_API_KEY}"
    
    if country:
        url = url + f"&country={country}"
    if category:
        url = url + f"&category={category}"
    print(url)
    res = requests.get(url)
    return res.json()

