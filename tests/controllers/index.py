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
        menu = {
            'test1': 'test1.html',
            'test2': 'test2.html',
            'test3': 'test3.html',
        }
        index = IndexController(menu)
        output_index = index.to_html()

        self.assertIn('Vítejte', output_index, 'string not found')
        self.assertIn('sedí doma', output_index, 'string not found')
        # tenhle test me dobehne

        self.assertIn('test1', output_index)
        self.assertIn('test2.html', output_index)
        self.assertIn('test3', output_index)

