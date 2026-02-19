import unittest

from nodes_and_blocks.textnode import TextNode, TextType
from functions.text_to_textnodes import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):
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
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
