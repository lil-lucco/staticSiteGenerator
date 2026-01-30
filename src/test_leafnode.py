import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_html(self):
        node = LeafNode("a", "Click me!")
        node.props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node.to_html()

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()