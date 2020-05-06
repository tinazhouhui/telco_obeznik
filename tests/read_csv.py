import unittest
from read_csv import articles

class TestReadCsv(unittest.TestCase):
    """
    Test basic CSV parsing functionality
    """

    def test_articles_empty(self):
        output = articles([])
        self.assertDictEqual(output, {}, 'The output is not empty dictionary')
