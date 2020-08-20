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


def get_sources():
    pass


def search_by_keyword(keyword):
    """Search article by keyword search engine."""
    everything = get_everything(keyword=keyword)
    return everything

