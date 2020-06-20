"""
Integration test.
"""

import unittest
from app.router import router


class TestRouter(unittest.TestCase):
    """
    Integration test for router.
    """

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
            },
            '2020-03': {
                'world': [
                    {
                        'title': '3 yup router',
                        'link': 'https://www.router.com',
                        'source': 'really 3 router',
                        'summary': 'an amazing 3 router',
                        'date': 'March 2020',
                    },
                ],
            },
            '2020-04': {
                'czech': [
                    {
                        'title': 'april router',
                        'link': 'https://www.router.co.uk',
                        'source': 'routers of april',
                        'summary': 'april fools router',
                        'date': 'April 2020',
                    },
                ],
            },
        }
        output = list(router(article_input).keys())
        expected_output = [
            'index.html',
            'archive.html',
            'january2020.html',
            'february2020.html',
            'march2020.html',
            'april2020.html',
        ]

        self.assertEqual(output, expected_output, "router is not assigning correct routes")
