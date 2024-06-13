from newsapi import NewsApiClient
from secret_settings.secret_globals import *


def get_top_news():
    # Init
    newsapi = NewsApiClient(api_key=NEWS_API_KEY)

    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(language='en',
                                              country='us')
    return top_headlines.get('articles')