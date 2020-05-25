"""
Unit test for input prep
"""
import unittest
from app.input_prep import validate_data, articles, pages


class TestReadCsv(unittest.TestCase):
    """
    Test data transformation formatting.
    """

    def test_validate_data_empty(self):
        """
        Test on empty imput should return empty output.
        """
        output = validate_data([])
        self.assertEqual(output, [], 'The output is not empty list')

    def test_validate_incorrect_link(self):
        """
        Test that link validator raises error when wrong data.
        """
        raw_data = [
            [
                'This is a title',
                'seznam.cz',
                'Senam.cz 2020',
                'summary of article',
                'December 2020',
            ]
        ]
        with self.assertRaises(TypeError) as error:
            validate_data(raw_data)
        self.assertEqual(str(error.exception), "seznam.cz is not a link")

    def test_validate_incorrect_date(self):
        """
        Test that date validator raises error when wrong data.
        """
        raw_data = [
            [
                'This is a title',
                'https://www.seznam.cz',
                'Senam.cz 2020',
                'summary of article',
                'December 2020',
            ]
        ]
        with self.assertRaises(TypeError) as error:
            validate_data(raw_data)
        self.assertEqual(str(error.exception), "December 2020 is not a date")

    def test_validate_correct_data(self):
        """
        Test that date validator lets correct data pass.
        """
        raw_data = [
            [
                'This is a title',
                'https://www.seznam.cz',
                'Senam.cz 2020',
                'summary of article',
                '20.02.2020',
            ]
        ]
        output = validate_data(raw_data)
        self.assertIs(raw_data, output)

    def test_articles_empty(self):
        """
        Test on empty imput should return empty output.
        """
        output = articles([])
        self.assertEqual(output, [], 'The output is not empty list')

    def test_articles_columns(self):
        """
        Test the correct formatting of date and connection to correct key.
        """
        article_input = [['col1', 'col2', 'col3', 'col4', '24.12.2020', 'col6']]
        output = articles(article_input)
        self.assertEqual(output[0]['title'], "col1")
        self.assertEqual(output[0]['link'], "col2")
        self.assertEqual(output[0]['source'], "col3")
        self.assertEqual(output[0]['summary'], "col4")
        self.assertEqual(output[0]['date'], "December 2020")
        self.assertEqual(len(output[0]), 5)

    def test_pages_empty(self):
        """
        Test on empty imput should return empty output.
        """
        output = pages({})
        self.assertEqual(output, {}, 'The output is not empty dictionary')

    def test_pages_keys(self):
        """
        Test that articles with same keys are appended together.
        """
        pages_input = [
            {
                'title':'col1',
                'link':'col2',
                'source':'col3',
                'summary':'col4',
                'date':'December 2020',
            },
            {
                'title':'col11',
                'link':'col22',
                'source':'col33',
                'summary':'col44',
                'date':'December 2020',
            },
        ]
        output = pages(pages_input)
        self.assertEqual(len(output), 1)
        self.assertEqual(list(output.keys())[0], 'December 2020')
