"""
Rendering of archive to html code.
"""

from app.controllers.base import BaseController


class ArchiveController(BaseController):
    """
    Class to render archive.
    """
    def __init__(self):
        super().__init__('Archiv')

    def to_html(self):
        """
        renders archive to an html string and creates one continuous string.
        """

        template = self.template_env.get_template("archive.html.j2")

        return template.render(
            title=self.title,
        )
