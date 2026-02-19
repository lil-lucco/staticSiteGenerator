import unittest

from functions.extract_markdown_links import extract_markdown_links


class TestExtractMarkdownLinks(unittest.TestCase):
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
        self.assertEqual(extract_markdown_links(input_text), expected)


if __name__ == "__main__":
    unittest.main()
