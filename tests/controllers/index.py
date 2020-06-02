"""
Unit test for index page.
"""
import unittest

from app.controllers.index import IndexController


class TestIndexController(unittest.TestCase):
    """
    Unit test for index rendering to html code.
    """

    def test_index(self):
        index = IndexController()
        output_index = index.to_html()

        self.assertIn('Vítejte', output_index, 'string not found')
        self.assertIn('sedí doma', output_index, 'string not found')
        # tenhle test me dobehne

