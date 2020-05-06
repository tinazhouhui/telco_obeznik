import unittest
from read_csv import articles

class TestReadCsv(unittest.TestCase):
    """
    Test basic CSV parsing functionality
    """

    def test_articles_empty(self):
        input = []

        print(articles)

        output = articles(input)
        print(output)
        self.assertEqual('foo'.upper(), 'F1OO')
