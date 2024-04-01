import unittest
import requests

class TestWebsiteConnection(unittest.TestCase):
    def test_website_connection(self):
        url = "https://atg.world"
        response = requests.get(url)
        status_code = response.status_code
        self.assertEqual(status_code, 200, f"Website {url} failed to load properly (Status Code: {status_code})")

if __name__ == "__main__":
    unittest.main()
