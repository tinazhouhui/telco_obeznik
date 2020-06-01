"""
Integration test.
"""

import unittest
from app.router import router


class TestRouter(unittest.TestCase):
    """
    Integration test for router.
    """
    def test_router_empty(self):
        """
        tests empty dictionary.
        """
        input = {}
        output = list(router(input).keys())

        self.assertEqual(output, ['index.html', 'archive.html'], "the router is not empty")

    def test_router_keys(self):
        """
        Integration test - testing only keys.
        """
        article_input: dict = {
            '2020-01': {
                'world': [
                    {
                        'title': 'this is router',
                        'link': 'https://www.router.io',
                        'source': 'best routers',
                        'summary': 'so many routers',
                        'date': 'January 2020',
                    },
                ],
            },
            '2020-02': {
                'czech': [
                    {
                        'title': 'still router',
                        'link': 'https://www.router.cz',
                        'source': 'really router',
                        'summary': 'an amazing router',
                        'date': 'February 2020',
                    },
                ],
            }
        }
        output = list(router(article_input).keys())
        expected_output = ['index.html', 'archive.html', 'january20.html', 'february20.html']

        self.assertEqual(output, expected_output, "router is not assigning correct routes")

