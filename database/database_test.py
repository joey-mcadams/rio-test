from database.db_engine import *


def test_get_and_slice_articles():
    peewee_db.connect()
    all_articles = Article.select()
    articles = all_articles[:5]
    article_format = """
                {title}

                {content}
                """

    for article in articles:
        print(article_format.format(title=article.title, content=article.content))

    peewee_db.close()

test_get_and_slice_articles()