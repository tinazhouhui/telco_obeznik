"""
Rendering of articles to html code.
"""

from app.controllers.base import BaseController


class ArticlesController(BaseController):
    """
    Class to render articles.
    """

    def __init__(self, menu: dict, title: str, article_list: dict):
        super().__init__(menu, title)
        self.article_list = article_list

    def to_html(self):
        """
        renders each article to an html string and creates one continuous string.
        """
        article_html: str = self.render(
            "articles.html.j2",
            article_list=self.article_list,
            archive_list=self.menu,
        )

        return article_html
