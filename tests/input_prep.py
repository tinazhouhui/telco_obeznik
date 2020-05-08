import unittest
import csv
from app.input_prep import read_csv, articles, pages
from datetime import datetime

class TestReadCsv(unittest.TestCase):
    """
    Test basic CSV parsing functionality
    """

    def test_articles_empty(self):
        output = articles([])
        self.assertEqual(output, [], 'The output is not empty list')

    def test_articles_columns(self):
        input = [['col1', 'col2', 'col3', 'col4', '24.12.2020', 'col6']]
        output = articles(input)
        self.assertEqual(output[0]['title'], "col1")
        self.assertEqual(output[0]['link'], "col2")
        self.assertEqual(output[0]['source'], "col3")
        self.assertEqual(output[0]['summary'], "col4")
        self.assertEqual(output[0]['date'], "December 2020")
        self.assertEqual(len(output[0]), 5)

    def test_pages_empty(self):
        output = pages({})
        self.assertEqual(output, {}, 'The output is not empty dictionary')

if __name__ == '__main__':
    help(input_prep)
    unittest.main()
