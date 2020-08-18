import os
from newsapi import NewsApiClient

NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
newsapi = NewsApiClient(api_key=os.environ.get('NEWS_API_KEY'))

def search_by_keyword(keyword):
    """Search article by keyword search engine."""
    top_headlines = newsapi.get_top_headlines(q=keyword)
    return top_headlines

