import unittest

from functions.markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = (
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p>"
            "<p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
        )
        self.assertEqual(html, expected)

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = (
            "<div><pre><code>This is text that _should_ remain\n"
            "the **same** even with inline stuff\n</code></pre></div>"
        )
        self.assertEqual(html, expected)

    def test_markdown_to_html_heading_block(self):
        md = "# Main Title"
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><h1>Main Title</h1></div>"
        self.assertEqual(html, expected)

    def test_markdown_to_html_quote_with_inline_formatting(self):
        md = "> first line\n> second **line**"
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><blockquote>first line second <b>line</b></blockquote></div>"
        self.assertEqual(html, expected)

    def test_markdown_to_html_unordered_list_with_inline_formatting(self):
        md = "- one\n- two _emph_"
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><ul><li>one</li><li>two <i>emph</i></li></ul></div>"
        self.assertEqual(html, expected)

    def test_markdown_to_html_ordered_list_block(self):
        md = "1. alpha\n2. beta\n3. gamma"
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = "<div><ol><li>alpha</li><li>beta</li><li>gamma</li></ol></div>"
        self.assertEqual(html, expected)

    def test_markdown_to_html_mixed_blocks(self):
        md = "# Title\n\n> quote line\n\n- item one\n- item two\n\nplain `code` text"
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = (
            "<div><h1>Title</h1><blockquote>quote line</blockquote>"
            "<ul><li>item one</li><li>item two</li></ul>"
            "<p>plain <code>code</code> text</p></div>"
        )
        self.assertEqual(html, expected)


if __name__ == "__main__":
    unittest.main()
