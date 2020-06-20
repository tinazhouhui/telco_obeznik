"""
Unit test for input prep
"""

import unittest

from app.models.output_prep import create_all_links, create_latest_page, create_menu, \
    create_archive_menu, create_latest_month


class TestReadCsv(unittest.TestCase):
    """
    Test data transformation formatting.
    """

    def test_create_all_links(self):
        """
        test to see that all links are generated.
        """

        pages_groups: dict = {
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
        output_keys = list(create_all_links(pages_groups).keys())
        output_values = len(list(create_all_links(pages_groups).values()))

        self.assertEqual(output_keys, ['April', 'March', 'February', 'January',], 'links not matching')
        self.assertEqual(output_values, 4, 'number of links not matching')

    def test_create_latest_page(self):
        """
        testing that only latest page is taken
        """
        all_links = {
            'April': 'april20.html',
            'March': 'march20.html',
            'February': 'february20.html',
        }

        output = create_latest_page(all_links)

        self.assertEqual(output, 'april20.html', 'not latest page')

    def test_create_latest_menu(self):
        """
        testing that only latest page name is taken
        """
        all_links = {
            'April': 'april20.html',
            'March': 'march20.html',
            'February': 'february20.html',
        }

        output = create_latest_month(all_links)

        self.assertEqual('April', output, "latest month not correct")



    def test_create_menu(self):
        """
        testing that menu has only three items and is correct
        """
        all_links = {
            'April': 'april20.html',
            'March': 'march20.html',
            'February': 'february20.html',
            'January': 'january20.html',
        }

        output_keys = list(create_menu(all_links).keys())
        output_values = list(create_menu(all_links).values())

        self.assertEqual(len(output_keys), 3, 'menu too long')
        self.assertEqual(output_keys, ['April', 'March', 'February'], "menu not correct")
        self.assertEqual(output_values, [
            'april20.html',
            'march20.html',
            'february20.html'
        ], "menu not correct")

    def test_create_archive_menu(self):
        """
        testing that archive menu has correct links assigned
        """

        all_links = {
            'Duben': 'april2020.html',
            'Květen': 'may2020.html',
            'Září': 'september2019.html',
        }

        output = create_archive_menu(all_links)

        self.assertEqual({
            '2020':{
                'Duben': 'april2020.html',
                'Květen': 'may2020.html',
            },
            '2019':{
                'Září': 'september2019.html',
            },
        }, output, "the archive is not correct")
