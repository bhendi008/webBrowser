import unittest
from browser import URL, HTMLParser, BlockLayout, DocumentLayout, Text, Element

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

class TestBlockLayout(unittest.TestCase):
    def test_layout_text(self):
        text = Text("hello",None)
        layout = BlockLayout(text, None, None)
        assert layout.layout_mode() == "inline"

    def test_layout_block(self):
        node = Element("div", {}, None)
        layout = BlockLayout(node, None, None)
        assert layout.layout_mode() == "block"

    def test_layout_children(self):
        parent = Element("div", {}, None)
        child = Element("p", {}, parent)

        parent.children.append(child)

        document = DocumentLayout(parent)
        document.layout()
        
        layout = document.children[0]

        self.assertEqual(len(layout.children), 1)
        self.assertIs(layout.children[0].node, child)

if __name__ == "__main__":
    unittest.main(verbosity=2)
