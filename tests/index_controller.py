"""
Unit test for index controller.
"""

import unittest
from app.index_controller import year_month_parsing, page_title, file_name


class TestReadCsv(unittest.TestCase):
    """
    Test correct parsing of index.
    """

    def test_year_month_parsing(self):
        """
        parse numbers into correct month name.
        """
        year_month = "1993-04"
        output = year_month_parsing(year_month)

        self.assertEqual(output, "April 1993", "month name not parsed correctly")

    def test_page_title(self):
        """
        parse numbers into page title.
        """
        year_name = "1993-04"
        output = page_title(year_name)

        self.assertEqual(output, "April", "title not correct")

    def test_filename(self):
        """
        parse numbers into filename.
        """
        year_name = "1993-04"
        output = file_name(year_name)

        self.assertEqual(output, "april93.html", "filename not correct")
