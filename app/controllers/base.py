"""
Base controller for html pages.
"""

import os

from jinja2 import FileSystemLoader, Environment


class BaseController:
    """
    Abstract class for all other controllers.
    """

    def __init__(self, menu: dict, title: str):
        self.menu = menu
        self.title = title
        template_path = os.path.dirname(__file__) + '/../views'
        template_loader = FileSystemLoader(searchpath=template_path)
        self.template_env = Environment(loader=template_loader, autoescape=True)

    def to_html(self) -> str:
        """
        base case, null object pattern.
        """
        return 'Implement me!'

    def render(self, template_path: str, **arguments) -> str:
        """
        renders arguments to jinja views.
        """
        template = self.template_env.get_template(template_path)

        return template.render(
            title=self.title,
            menu=self.menu,
            **arguments,
        )
