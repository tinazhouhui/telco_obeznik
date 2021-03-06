"""
Unit test for render that checks the correct rendering.
"""
import unittest
from app.controllers.articles import ArticlesController


class TestArticlesController(unittest.TestCase):
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
        menu = {
            'test1': 'test1.html',
            'test2': 'test2.html',
            'test3': 'test3.html',
        }

        articles = ArticlesController(menu, title, article_list)
        output_articles = articles.to_html()
        self.assertIn(article_list['world'][0]['title'], output_articles)
        self.assertIn(article_list['world'][0]['link'], output_articles)
        self.assertIn(article_list['world'][0]['source'], output_articles)
        self.assertIn(article_list['world'][0]['summary'], output_articles)
        self.assertIn(article_list['czech'][0]['title'], output_articles)
        self.assertIn(article_list['czech'][0]['link'], output_articles)
        self.assertIn(article_list['czech'][0]['source'], output_articles)
        self.assertIn(article_list['czech'][0]['summary'], output_articles)

        self.assertIn(title, output_articles)

        self.assertIn('test1', output_articles)
        self.assertIn('test2', output_articles)
        self.assertIn('test3.html', output_articles)
