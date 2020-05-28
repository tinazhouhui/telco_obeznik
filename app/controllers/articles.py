"""
Rendering of articles to html code.
"""

from app.controllers.base import BaseController


class ArticlesController(BaseController):
    """
    Class to render articles.
    """

    def __init__(self, title: str, article_list):
        super().__init__(title)

        self.article_list = article_list

    def to_html(self):
        """
        renders each article to an html string and creates one continuous string.
        """

        template = self.template_env.get_template("articles.html.j2")

        return template.render(
            article_list=self.article_list,
            title=self.title,
        )
