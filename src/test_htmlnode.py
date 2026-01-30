import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode()
        node.props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node.props_to_html()
    def test_no_props(self):
        node = HTMLNode()
        node.props = None
        node.props_to_html()

if __name__ == "__main__":
    unittest.main()