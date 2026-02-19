import unittest

from functions.extract_markdown_images import extract_markdown_images


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        input_text = (
            "Gallery: ![logo](https://img.example.com/logo.png) "
            "and ![banner](https://img.example.com/banner.jpg)"
        )
        expected = [
            ("logo", "https://img.example.com/logo.png"),
            ("banner", "https://img.example.com/banner.jpg"),
        ]
        self.assertEqual(extract_markdown_images(input_text), expected)


if __name__ == "__main__":
    unittest.main()
