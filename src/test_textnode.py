import unittest
from textnode import TextNode, TextType
from functions import *
from blocks import markdown_to_blocks


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
        input_text = (
            "Gallery: ![logo](https://img.example.com/logo.png) "
            "and ![banner](https://img.example.com/banner.jpg)"
        )
        expected = [
            ("logo", "https://img.example.com/logo.png"),
            ("banner", "https://img.example.com/banner.jpg"),
        ]
        matches = extract_markdown_images(input_text)
        self._assert_with_failure_debug(
            "test_extract_markdown_images",
            input_text,
            matches,
            expected,
        )
    
    def test_extract_markdown_links(self):
        input_text = (
            "See [Google](https://www.google.com), "
            "watch [Boot.dev](https://www.youtube.com/@bootdotdev), "
            "and ignore ![logo](https://img.example.com/logo.png)"
        )
        expected = [
            ("Google", "https://www.google.com"),
            ("Boot.dev", "https://www.youtube.com/@bootdotdev"),
        ]
        matches = extract_markdown_links(input_text)
        self._assert_with_failure_debug(
            "test_extract_markdown_links",
            input_text,
            matches,
            expected,
        )

    def test_split_nodes_image_lesson_example(self):
        old_nodes = [
            TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) "
                "and another ![second image](https://i.imgur.com/3elNhQu.png)",
                TextType.TEXT,
            )
        ]
        result = split_nodes_image(old_nodes)
        expected = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ]
        self._assert_with_failure_debug(
            "test_split_nodes_image_lesson_example",
            old_nodes,
            result,
            expected,
        )

    def test_split_nodes_image_no_images_returns_original_text_node(self):
        old_nodes = [TextNode("Just plain text here.", TextType.TEXT)]
        result = split_nodes_image(old_nodes)
        expected = [TextNode("Just plain text here.", TextType.TEXT)]
        self._assert_with_failure_debug(
            "test_split_nodes_image_no_images_returns_original_text_node",
            old_nodes,
            result,
            expected,
        )

    def test_split_nodes_image_start_and_end_no_empty_text_nodes(self):
        old_nodes = [
            TextNode(
                "![start](https://img.example.com/start.png) middle "
                "![end](https://img.example.com/end.png)",
                TextType.TEXT,
            )
        ]
        result = split_nodes_image(old_nodes)
        expected = [
            TextNode("start", TextType.IMAGE, "https://img.example.com/start.png"),
            TextNode(" middle ", TextType.TEXT),
            TextNode("end", TextType.IMAGE, "https://img.example.com/end.png"),
        ]        
        self._assert_with_failure_debug(
            "test_split_nodes_image_start_and_end_no_empty_text_nodes",
            old_nodes,
            result,
            expected,
        )

    def test_split_nodes_image_ignores_non_text_nodes(self):
        old_nodes = [
            TextNode("Already link", TextType.LINK, "https://www.boot.dev"),
            TextNode(
                "then ![pic](https://img.example.com/pic.jpg)",
                TextType.TEXT,
            ),
        ]
        result = split_nodes_image(old_nodes)
        expected = [
            TextNode("Already link", TextType.LINK, "https://www.boot.dev"),
            TextNode("then ", TextType.TEXT),
            TextNode("pic", TextType.IMAGE, "https://img.example.com/pic.jpg"),
        ]
        self._assert_with_failure_debug(
            "test_split_nodes_image_ignores_non_text_nodes",
            old_nodes,
            result,
            expected,
        )

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
        self._assert_with_failure_debug(
            "test_split_nodes_link_lesson_example",
            old_nodes,
            result,
            expected,
        )

    def test_split_nodes_link_no_links_returns_original_text_node(self):
        old_nodes = [TextNode("Just plain text, no links.", TextType.TEXT)]
        result = split_nodes_link(old_nodes)
        expected = [TextNode("Just plain text, no links.", TextType.TEXT)]
        self._assert_with_failure_debug(
            "test_split_nodes_link_no_links_returns_original_text_node",
            old_nodes,
            result,
            expected,
        )

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
        self._assert_with_failure_debug(
            "test_split_nodes_link_start_and_end_no_empty_text_nodes",
            old_nodes,
            result,
            expected,
        )

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
        self._assert_with_failure_debug(
            "test_split_nodes_link_ignores_non_text_nodes",
            old_nodes,
            result,
            expected,
        )

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
        self._assert_with_failure_debug(
            "test_split_nodes_link_does_not_treat_images_as_links",
            old_nodes,
            result,
            expected,
        )

    def test_text_to_textnodes(self):
        text = [
            TextNode(
                "This is **text** with an _italic_ word and a `code block` and " 
                "an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and " 
                "a [link](https://boot.dev)",
                TextType.TEXT,
            )
        ]
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        # print(f"result: {result}")
        # print(f"expected: {expected}")
        self._assert_with_failure_debug(
            "test_text_to_textnodes",
            text,
            result,
            expected,
        )

    # test to fix:
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

if __name__ == "__main__":
    unittest.main()
