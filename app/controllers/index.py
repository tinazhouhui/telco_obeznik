"""
Rendering of index to html code.
"""

from app.controllers.base import BaseController


class IndexController(BaseController):
    """
    Class to render index.
    """

    def __init__(self):
        super().__init__('Vítejte na Telco oběžníku!')
        self.description = 'sedí doma, píšou nabídky a už netrefí do práce'

    def to_html(self):
        """
        renders each article to an html string and creates one continuous string.
        """

        template = self.template_env.get_template("index.html.j2")

        return template.render(
            title=self.title,
            description = self.description
        )
