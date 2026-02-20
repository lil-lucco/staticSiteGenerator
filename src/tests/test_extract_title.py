import unittest

from functions.extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extracts_title_from_single_h1_line(self):
        markdown = "# Hello World"
        self.assertEqual(extract_title(markdown), "Hello World")

    def test_extracts_first_h1_from_multiline_markdown(self):
        markdown = "intro text\n# First Title\n## Subtitle\n# Second Title"
        self.assertEqual(extract_title(markdown), "First Title")

    def test_raises_when_h1_not_found(self):
        markdown = "## Not H1\nplain paragraph"
        with self.assertRaisesRegex(Exception, "h1 header not found"):
            extract_title(markdown)

    def test_raises_type_error_for_non_string_input(self):
        with self.assertRaisesRegex(TypeError, "requires str input"):
            extract_title(None)


if __name__ == "__main__":
    unittest.main()
