import unittest

from nodes_and_blocks.textnode import TextNode, TextType
from functions.split_nodes_delimiter import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_code_single_segment(self):
        old_nodes = [TextNode("This is text with a `code block` word", TextType.TEXT)]
        result = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_ignores_non_text_nodes(self):
        old_nodes = [TextNode("already bold", TextType.BOLD)]
        result = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        self.assertEqual(result, old_nodes)

    def test_split_nodes_delimiter_multiple_segments(self):
        old_nodes = [TextNode("start `one` mid `two` end", TextType.TEXT)]
        result = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        expected = [
            TextNode("start ", TextType.TEXT),
            TextNode("one", TextType.CODE),
            TextNode(" mid ", TextType.TEXT),
            TextNode("two", TextType.CODE),
            TextNode(" end", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_raises_on_unbalanced_delimiter(self):
        old_nodes = [TextNode("This has `broken markdown", TextType.TEXT)]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(old_nodes, "`", TextType.CODE)


if __name__ == "__main__":
    unittest.main()
