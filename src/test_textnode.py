import unittest

from textnode import TextNode, TextType
from functions import text_node_to_html_node, split_nodes_delimiter, extract_markdown_images, extract_markdown_links


class TestTextNode(unittest.TestCase):
    def _assert_with_failure_debug(self, test_name, input_value, result, expected):
        try:
            self.assertEqual(result, expected)
        except AssertionError:
            print(f"\n[{test_name}]")
            print(f"input:    {input_value}")
            print(f"result:   {result}")
            print(f"expected: {expected}")
            raise
        else:
            print(f"{test_name} TEST PASSED!")

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("testing None URL", TextType.LINK)
        node2 = TextNode("testing None URL", TextType.LINK, "https://www.google.com")
        self.assertNotEqual(node, node2)
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    # Baseline case from the lesson: one delimited segment in the middle.
    def test_split_nodes_delimiter_code_single_segment(self):
        old_nodes = [TextNode("This is text with a `code block` word", TextType.TEXT)]
        result = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self._assert_with_failure_debug(
            "test_split_nodes_delimiter_code_single_segment",
            old_nodes,
            result,
            expected,
        )

    # Non-TEXT nodes should be passed through untouched.
    def test_split_nodes_delimiter_ignores_non_text_nodes(self):
        old_nodes = [TextNode("already bold", TextType.BOLD)]
        result = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        self._assert_with_failure_debug(
            "test_split_nodes_delimiter_ignores_non_text_nodes",
            old_nodes,
            result,
            old_nodes,
        )

    # Multiple delimiter pairs should alternate plain/formatted/plain correctly.
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
        self._assert_with_failure_debug(
            "test_split_nodes_delimiter_multiple_segments",
            old_nodes,
            result,
            expected,
        )

    # Unbalanced markdown should raise, so bad content can be rejected early.
    def test_split_nodes_delimiter_raises_on_unbalanced_delimiter(self):
        old_nodes = [TextNode("This has `broken markdown", TextType.TEXT)]
        test_name = "test_split_nodes_delimiter_raises_on_unbalanced_delimiter"
        try:
            with self.assertRaises(ValueError):
                split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        except AssertionError:
            print(f"\n[{test_name}]")
            print(f"input:    {old_nodes}")
            print("result:   ValueError was not raised")
            raise
        else:
            print(f"{test_name} TEST PASSED!")

    # example test given by course
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.google.com)"
        )
        self.assertListEqual([("link", "https://www.google.com")], matches)


if __name__ == "__main__":
    unittest.main()
