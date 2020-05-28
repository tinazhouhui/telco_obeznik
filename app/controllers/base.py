"""
Base controller for html pahes.
"""
import os
from jinja2 import FileSystemLoader, Environment


class BaseController:
    """
    Basic page renderer
    """

    def __init__(self, title: str):
        self.title = title
        template_path = os.path.dirname(__file__) + '/../views'
        template_loader = FileSystemLoader(searchpath=template_path)
        self.template_env = Environment(loader=template_loader, autoescape=True)

    def to_html(self) -> str:
        return 'Implement me!'
