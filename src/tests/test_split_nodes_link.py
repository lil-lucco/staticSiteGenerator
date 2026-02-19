import unittest

from nodes_and_blocks.textnode import TextNode, TextType
from functions.split_nodes_link import split_nodes_link


class TestSplitNodesLink(unittest.TestCase):
    def test_split_nodes_link_lesson_example(self):
        old_nodes = [
            TextNode(
                "This is text with a [link](https://reddit.com) "
                "and another [second link](https://python.org)",
                TextType.TEXT,
            )
        ]
        result = split_nodes_link(old_nodes)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://reddit.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second link", TextType.LINK, "https://python.org"),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_link_no_links_returns_original_text_node(self):
        old_nodes = [TextNode("Just plain text, no links.", TextType.TEXT)]
        result = split_nodes_link(old_nodes)
        expected = [TextNode("Just plain text, no links.", TextType.TEXT)]
        self.assertEqual(result, expected)

    def test_split_nodes_link_start_and_end_no_empty_text_nodes(self):
        old_nodes = [
            TextNode(
                "[start](https://example.com/start) middle "
                "[end](https://example.com/end)",
                TextType.TEXT,
            )
        ]
        result = split_nodes_link(old_nodes)
        expected = [
            TextNode("start", TextType.LINK, "https://example.com/start"),
            TextNode(" middle ", TextType.TEXT),
            TextNode("end", TextType.LINK, "https://example.com/end"),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_link_ignores_non_text_nodes(self):
        old_nodes = [
            TextNode("already image", TextType.IMAGE, "https://img.example.com/pic.jpg"),
            TextNode(
                "then [docs](https://docs.example.com)",
                TextType.TEXT,
            ),
        ]
        result = split_nodes_link(old_nodes)
        expected = [
            TextNode("already image", TextType.IMAGE, "https://img.example.com/pic.jpg"),
            TextNode("then ", TextType.TEXT),
            TextNode("docs", TextType.LINK, "https://docs.example.com"),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_link_does_not_treat_images_as_links(self):
        old_nodes = [
            TextNode(
                "Image ![logo](https://img.example.com/logo.png) "
                "and link [site](https://www.boot.dev)",
                TextType.TEXT,
            )
        ]
        result = split_nodes_link(old_nodes)
        expected = [
            TextNode(
                "Image ![logo](https://img.example.com/logo.png) and link ",
                TextType.TEXT,
            ),
            TextNode("site", TextType.LINK, "https://www.boot.dev"),
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
