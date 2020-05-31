"""
Integration test.
"""

import unittest
from app.router import router


class TestRouter(unittest.TestCase):
    def test_router_empty(self):
        input = {}
        output = list(router(input).keys())

        self.assertEqual(output, ['index.html', 'archive.html'], "the router is not empty")
