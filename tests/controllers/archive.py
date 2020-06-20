"""
Unit test for archive page.
"""
import unittest

from app.controllers.archive import ArchiveController
from app.models.output_prep import create_menu, create_archive_menu


class TestArchiveController(unittest.TestCase):
    """
    Unit test for archive rendering to html code.
    """

    def test_archive(self):
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
        archive_menu = create_archive_menu(all_menu)

        archive = ArchiveController(menu, archive_menu)
        output_index = archive.to_html()

        self.assertIn('test1', output_index)
        self.assertIn('test2.html', output_index)
        self.assertIn('test3', output_index)
        self.assertIn('test4.html', output_index)
