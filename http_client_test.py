import json
import unittest

import http_client

import bot


class MyTestCase(unittest.TestCase):
    def test_post(self):
        response = json.loads(http_client.post("https://api.m3o.com/v1/answer/Question", {'query': "youtube"}, bot.M3O_API_TOKEN).replace('\\', ''))
        self.assertEqual(response["url"], "https://en.wikipedia.org/wiki/YouTube")

    def test_request(self):
        response = http_client.request("api.m3o.com", "GET / HTTP/1.0\r\nHost: api.m3o.com\r\n\r\n")
        self.assertEqual("unauthorized request" in response, True)

if __name__ == '__main__':
    unittest.main()
