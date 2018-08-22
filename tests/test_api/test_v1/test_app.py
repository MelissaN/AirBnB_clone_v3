#!/usr/bin/python3
"""
Testing app.py
"""
import unittest
import flask
from api.v1.app import app
from models import storage
import json


class Test_App(unittest.TestCase):
    """Testing app.py"""
    def setUp(self):
        """setup"""
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        """teardown"""
        pass

    def test_404(self):
        """test @app.errorhandler(404)"""
        response = self.app.get('/fake_route')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'{"error":"Not found"}', response.data)


if __name__ == "__main__":
    unittest.main()
