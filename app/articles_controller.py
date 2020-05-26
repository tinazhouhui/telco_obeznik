"""
Rendering of articles to html code.
"""
import os
from jinja2 import FileSystemLoader, Environment


class ArticlesController:
    """
    Class to render articles.
    """

    def __init__(self, article_list, title: str):
        self.article_list = article_list
        self.title = title
        template_path = os.path.dirname(__file__) + '/templates'
        template_loader = FileSystemLoader(searchpath=template_path)
        self.template_env = Environment(loader=template_loader, autoescape=True)

    def to_html(self):
        """
        renders each article to an html string and creates one continuous string.
        """

        template = self.template_env.get_template("articles_body.html.j2")

        return template.render(
            article_list=self.article_list,
            title=self.title,
        )
