import unittest
from browser import URL, HTMLParser

class TestURL(unittest.TestCase):
    def test_http_url(self):
        url = URL("http://example.com/test")
        self.assertEqual(url.scheme, "http")
        self.assertEqual(url.host, "example.com")
        self.assertEqual(url.port, 80)
        self.assertEqual(url.path, "/test")

class TestHTMLParser(unittest.TestCase):
    def test_html_parser(self):
        tree = HTMLParser("<html><body>hello</body></html>").parse()
        body = tree.children[0]

        self.assertEqual(body.tag, "body")
        self.assertEqual(body.children[0].text, "hello")

if __name__ == "__main__":
    unittest.main()
