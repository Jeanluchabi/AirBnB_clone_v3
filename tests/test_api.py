#!/usr/bin/python3
import os
import unittest
import requests

class TestAPI(unittest.TestCase):
    API_URL = 'http://localhost:5000/api/v1'

    def test_status_endpoint(self):
        response = requests.get(f'{self.API_URL}/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "OK"})

    def test_stats_endpoint(self):
        response = requests.get(f'{self.API_URL}/stats')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json(), dict))

if __name__ == '__main__':
    unittest.main()

