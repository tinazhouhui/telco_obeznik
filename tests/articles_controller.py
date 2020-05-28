"""
Unit test for render that checks the correct rendering.
"""
import unittest
from app.controllers.articles import ArticlesController


class TestArticleListRender(unittest.TestCase):
    """
    Unit test for article rendering to html code.
    """

    def test_article_render(self):
        """
        Test that all inputs are somewhere in the html code.
        """
        article_list = {
            'world': [
                {
                    'title': 'Why am I awesome',
                    'link': 'https://www.tinaisawesome.io',
                    'source': 'Me, myself and I, 2020',
                    'summary': 'I just am. Duh.',
                    'date': 'January 2020',
                },
            ],
            'czech': [
                {
                    'title': 'Why',
                    'link': 'https://www.tinaisawesome.cz',
                    'source': 'Me',
                    'summary': 'I',
                    'date': 'February 2020',
                },
            ],
        }
        title = 'Month 2020'
        articles = ArticlesController(title, article_list)
        self.assertIn(article_list['world'][0]['title'], articles.to_html())
        self.assertIn(article_list['world'][0]['link'], articles.to_html())
        self.assertIn(article_list['world'][0]['source'], articles.to_html())
        self.assertIn(article_list['world'][0]['summary'], articles.to_html())
        self.assertIn(article_list['czech'][0]['title'], articles.to_html())
        self.assertIn(article_list['czech'][0]['link'], articles.to_html())
        self.assertIn(article_list['czech'][0]['source'], articles.to_html())
        self.assertIn(article_list['czech'][0]['summary'], articles.to_html())

        self.assertIn(title, articles.to_html())
