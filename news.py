import os
import requests
import json
# import pycurl
# from io import BytesIO

NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

# def get_json_url(url):
#     buffer = BytesIO()
#     c = pycurl.Curl()
#     c.setopt(c.URL, url)
#     c.setopt(c.IPRESOLVE, pycurl.IPRESOLVE_V4)
#     c.setopt(c.WRITEDATA, buffer)
#     c.perform()
#     c.close()
#     res = json.loads(buffer.getvalue())
#     return res


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

    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})
    api_articles = res.json()['articles']

    # api_articles = get_json_url(url)['articles']
    
    articles = convert_json(api_articles)
    return articles


#TODO limit results
def get_everything(keyword):
    """converts json response - for everything endpoint"""
    url = ( 'http://newsapi.org/v2/everything?' +
            'language=en' +
            '&q=' + keyword +
            '&apiKey=' + NEWS_API_KEY)

    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})
    api_articles = res.json()['articles']

    # api_articles = get_json_url(url)['articles']
        
    articles = convert_json(api_articles)
    
    return articles