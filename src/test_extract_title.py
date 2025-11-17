import unittest

from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_returns_first_top_level_heading(self):
        markdown = "# Hello World\nSome text\n## Subheading"
        self.assertEqual(extract_title(markdown), "Hello World")

    def test_ignores_leading_whitespace_before_heading(self):
        markdown = "Intro text\n   # Trimmed Title  \nMore text"
        self.assertEqual(extract_title(markdown), "Trimmed Title")

    def test_raises_when_no_heading_present(self):
        with self.assertRaises(ValueError):
            extract_title("Plain text with no headings at all.")


if __name__ == "__main__":
    unittest.main()
