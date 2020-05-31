"""
Rendering of articles to html code.
"""

from app.controllers.base import BaseController


class IndexController(BaseController):
    """
    Class to render articles.
    """

    def __init__(self):
        super().__init__('Vítejte na Telco oběžníku!')

    def to_html(self):
        """
        renders each article to an html string and creates one continuous string.
        """

        template = self.template_env.get_template("index.html.j2")

        return template.render(
            title=self.title,
        )
