import unittest
import csv
from app.input_prep import articles, pages
from datetime import datetime

class TestReadCsv(unittest.TestCase):
    """
    Test basic CSV parsing functionality
    """

    def test_articles_empty(self):
        output = articles([])
        self.assertEqual(output, [], 'The output is not empty list')

    def test_pages_empty(self):
        output = pages({})
        self.assertEqual(output, {}, 'The output is not empty dictionary')

if __name__ == '__main__':
    help(input_prep)
    unittest.main()
