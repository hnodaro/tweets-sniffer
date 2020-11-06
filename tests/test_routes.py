import unittest
import requests

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.URL = "http://localhost:5000"

    def test_home_get(self):
        r = requests.get(self.URL)
        self.assertIn("<h2 class=\"mt-20 mb-40 small\">Tweets Scrapper</h2>", r.text)
        self.assertEquals(r.status_code, 200)

    def test_home_post(self):
        payload = {'username': 'realDonaldTrump', 'limit': '5'}
        r = requests.post(self.URL, data = payload)
        self.assertIn("<table border=\"0\" class=\"dataframe table table-striped table-bordered table-hover\">", r.text)
        self.assertEquals(r.status_code, 200)

    def test_home_post_error(self):
        payload = {'username': 'jfhsldfhskfbb', 'limit': '5'}
        r = requests.post(self.URL, data = payload)
        self.assertIn("Username: jfhsldfhskfbb doesn&#39;t exist on Twitter", r.text)
        self.assertEquals(r.status_code, 200)