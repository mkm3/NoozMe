import os
import requests

NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    

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

    res = requests.get(url)
    api_articles = res.json()['articles']
    
    articles = convert_json(api_articles)
    return articles


#TODO limit results
def get_everything(keyword):
    """converts json response - for everything endpoint"""
    url = ( 'http://newsapi.org/v2/everything?' +
            'language=en' +
            '&q=' + keyword +
            '&apiKey=' + NEWS_API_KEY)

    res = requests.get(url)
    api_articles = res.json()['articles']
        
    articles = convert_json(api_articles)
    
    #for testing
    print(articles)
    return articles


