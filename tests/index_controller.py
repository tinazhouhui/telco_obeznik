"""
Unit test for index controller.
"""

import unittest
from app.index_controller import year_month_parsing, page_title, filename

class TestReadCsv(unittest.TestCase):
    """
    Test correct parsing of index.
    """

    def test_year_month_parsing(self):
        input = "1993-04"
        output = year_month_parsing(input)

        self.assertEqual(output, "April 1993", "month name not parsed correctly")

    def test_page_title(self):
        input = "1993-04"
        output = page_title(input)

        self.assertEqual(output, "April", "title not correct")

    def test_filename(self):
        input = "1993-04"
        output = filename(input)

        self.assertEqual(output, "april93.html", "filename not correct")


