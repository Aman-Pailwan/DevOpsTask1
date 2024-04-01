import unittest
import requests

class TestWebsiteConnection(unittest.TestCase):
    def test_website_connection(self):
        url = "https://atg.world"
        print(f"Connecting to {url}...")
        response = requests.get(url)
        status_code = response.status_code
        if status_code == 200:
            print(f"Success: Website {url} loaded properly (Status Code: {status_code})")
        else:
            print(f"Error: Website {url} failed to load properly (Status Code: {status_code})")

if __name__ == "__main__":
    print("Starting unit tests...")
    unittest.main()
