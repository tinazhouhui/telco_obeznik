"""
Rendering of index to html code.
"""

from app.controllers.base import BaseController


class IndexController(BaseController):
    """
    Class to render index.
    """

    def __init__(self, menu: dict):
        super().__init__(menu, 'Vítejte na Telco oběžníku!')
        self.description = 'sedí doma, píšou nabídky a už netrefí do práce'

    def to_html(self):
        """
        renders each article to an html string and creates one continuous string.
        """
        index_html = self.render(
            "index.html.j2",
            description=self.description,
        )

        return index_html
