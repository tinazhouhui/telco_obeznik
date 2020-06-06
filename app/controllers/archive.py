"""
Rendering of archive to html code.
"""

from app.controllers.base import BaseController


class ArchiveController(BaseController):
    """
    Class to render archive.
    """
    def __init__(self, menu: dict, menu_all: dict):
        super().__init__(menu, 'Archiv')
        self.menu_all = menu_all

    def to_html(self):
        """
        renders archive to an html string and creates one continuous string.
        """

        return self.render(
            "archive.html.j2",
            archive_list=self.menu_all,
        )
