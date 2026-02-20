import unittest

from functions.generate_page import generate_page


class TestGeneratePage(unittest.TestCase):
    def test_generate_page(self):
        from_path = "/from/path"  #FIXME
        template_path = "/template/path" #FIXME
        dest_path = "/dest/path" #FIXME
        self.assertEqual(generate_page(from_path, template_path, dest_path), "Hello World")

    

    # def test_extracts_first_h1_from_multiline_markdown(self):
    #     markdown = "intro text\n# First Title\n## Subtitle\n# Second Title"
    #     self.assertEqual(extract_title(markdown), "First Title")

    # def test_raises_when_h1_not_found(self):
    #     markdown = "## Not H1\nplain paragraph"
    #     with self.assertRaisesRegex(Exception, "h1 header not found"):
    #         extract_title(markdown)

    # def test_raises_type_error_for_non_string_input(self):
    #     with self.assertRaisesRegex(TypeError, "requires str input"):
    #         extract_title(None)


if __name__ == "__main__":
    unittest.main()
