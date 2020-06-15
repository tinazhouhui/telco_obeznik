"""
Unit test for index page.
"""
import unittest

from app.controllers.index import IndexController
from app.models.output_prep import create_menu, create_latest_page


class TestIndexController(unittest.TestCase):
    """
    Unit test for index rendering to html code.
    """

    def test_index(self):
        """
        Test index on all input values.
        """
        all_menu = {
            'test1': 'test1.html',
            'test2': 'test2.html',
            'test3': 'test3.html',
            'test4': 'test4.html'
        }
        menu = create_menu(all_menu)
        link = create_latest_page(all_menu)

        index = IndexController(menu, link)
        output_index = index.to_html()

        self.assertIn('Vítejte', output_index, 'string not found')
        self.assertIn('těší se na sud piva', output_index, 'description string not found')
        # tenhle test me dobehne

        self.assertIn('test1', output_index)
        self.assertIn('test2.html', output_index)
        self.assertIn('test3', output_index)
        self.assertNotIn('test4', output_index, 'menu not correct')
