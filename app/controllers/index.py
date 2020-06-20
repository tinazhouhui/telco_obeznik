"""
Rendering of index to html code.
"""

from app.controllers.base import BaseController


class IndexController(BaseController):
    """
    Class to render index.
    """

    def __init__(self, menu: dict, link: str, month: str):
        super().__init__(menu, 'Vítejte na Telco oběžníku!')
        self.description = 'v tuto chvíli píšou nabídky z domova, těší se na sud piva a už netrefí do práce'
        self.link = link
        self.month = month

    def to_html(self) -> str:
        """
        renders each article to an html string and creates one continuous string.
        """
        index_html = self.render(
            "index.html.j2",
            description=self.description,
            link=self.link,
            month=self.month
        )

        return index_html
