from database.db_engine import Author, Article
from news_aggregator.get_news import get_top_news
from openai import OpenAI
from secret_settings.secret_globals import OPEN_AI_KEY


client = OpenAI(api_key=OPEN_AI_KEY)


def make_top_articles():
    articles = get_top_news()
    authors = Author.select()

    # TODO: Randomly distribute stories
    author_index = 0
    author_size = len(authors)
    author = authors[0]

    for article in articles:
        # Skip these
        if article.get('title') == "[Removed]":
            continue

        new_title = article.get('title').split(" - ")

        model = "gpt-3.5-turbo"
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": f"You are {author.style}. You're here to report on the news"},
                {"role": "user", "content": f"write an article about \"{new_title}\""}
            ]
        )

        title_completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": f"You are {author.style}. You're here to report on the news"},
                {"role": "user", "content": f"Rewrite the following title \"{new_title}\""}
            ]
        )

        Article.create(title=title_completion.choices[0].message.content,
                       content=completion.choices[0].message.content,
                       author=author)

        # Next author
        author_index += 1
        if author_index > author_size - 1:
            author_index = 0

        author = authors[author_index]


