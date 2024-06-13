from __future__ import annotations

from dataclasses import KW_ONLY, field
from typing import *  # type: ignore

import rio

from database.db_engine import *
from .. import components as comps

class NewsPage(rio.Component):
    """
    A sample page, containing recent news articles about the company.
    """

    def build(self) -> rio.Component:
        # TODO: Optimize this, it's going to be slow as hell after a while.
        all_articles = Article.select()
        articles = all_articles[-5:]
        article_format = """# {title}
        
## by {author}
        
{content}
"""
        article_content = []
        for article in articles:
            new_text = article_format.format(title=article.title, content=article.content, author=article.author.author_name)
            article_content.append(new_text)

        return rio.Column(
            rio.Text("Recent News", style="heading1"),
            comps.NewsArticle(
                article_content[0]
            ),
            comps.NewsArticle(
                article_content[1]
            ),
            comps.NewsArticle(
                article_content[2]
            ),
            comps.NewsArticle(
                article_content[3]
            ),
            comps.NewsArticle(
                article_content[4]
            ),
            spacing=2,
            width=60,
            margin_bottom=4,
            align_x=0.5,
            align_y=0,
        )



