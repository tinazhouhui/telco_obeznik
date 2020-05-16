"""
Rendering of articles to html code.
"""
from jinja2 import FileSystemLoader, Environment
import os

class ArticleListRender:
    """
    Class to render articles.
    """

    def __init__(self, article_list):
        self.article_list = article_list
        template_path = os.path.dirname(__file__)+'/templates'
        template_loader = FileSystemLoader(searchpath=template_path)
        self.template_env = Environment(loader=template_loader)

    def to_html(self):
        """
        renders each article to an html string and creates one continuous string.
        """

        template = self.template_env.get_template("article_list.j2")
        return template.render(article_list = self.article_list)
