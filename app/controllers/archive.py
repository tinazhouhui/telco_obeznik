"""
Rendering of archive to html code.
"""

from app.controllers.base import BaseController


class ArchiveController(BaseController):
    """
    Class to render archive.
    """
    def __init__(self, menu: dict):
        super().__init__(menu, 'Archiv')

    def to_html(self):
        """
        renders archive to an html string and creates one continuous string.
        """

        return self.render("archive.html.j2")
