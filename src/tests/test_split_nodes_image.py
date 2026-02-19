import unittest

from nodes_and_blocks.textnode import TextNode, TextType
from functions.split_nodes_image import split_nodes_image


class TestSplitNodesImage(unittest.TestCase):
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
        self.assertEqual(result, expected)

    def test_split_nodes_image_no_images_returns_original_text_node(self):
        old_nodes = [TextNode("Just plain text here.", TextType.TEXT)]
        result = split_nodes_image(old_nodes)
        expected = [TextNode("Just plain text here.", TextType.TEXT)]
        self.assertEqual(result, expected)

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
        self.assertEqual(result, expected)

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
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
