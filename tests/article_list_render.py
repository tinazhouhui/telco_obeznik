"""
Unit test for render that checks the correct rendering.
"""
import unittest
from app.article_list_render import ArticleListRender

class TestArticleListRender(unittest.TestCase):

    def test_article_render(self):
        article_list = [

                    {
                        'title': 'Why am I awesome',
                        'link': 'https://www.tinaisawesome.io',
                        'source': 'Me, myself and I, 2020',
                        'summary': 'I just am. Duh.',
                        'date': 'January 2020',
                    }, {
                        'title': 'Why',
                        'link': 'https://www.tinaisawesome.cz',
                        'source': 'Me',
                        'summary': 'I',
                        'date': 'February 2020',
                    },
                ]

        articles = ArticleListRender(article_list)
        self.assertIn(article_list[0]['title'], articles.to_html())
        self.assertIn(article_list[0]['link'], articles.to_html())
        self.assertIn(article_list[0]['source'], articles.to_html())
        self.assertIn(article_list[0]['summary'], articles.to_html())
