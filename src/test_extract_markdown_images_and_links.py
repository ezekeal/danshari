import unittest

from extract_markdown_images_and_links import (
    extract_markdown_images,
    extract_markdown_links,
)


class TestExtractMarkdownImagesAndLinks(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")],
            matches,
        )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "Visit [Example](https://www.example.com) for more info"
        )
        self.assertListEqual(
            [("Example", "https://www.example.com")],
            matches,
        )

    def test_images_do_not_extract_links(self):
        matches = extract_markdown_images(
            "A regular [link](https://www.example.com) should not match"
        )
        self.assertListEqual([], matches)

    def test_links_do_not_extract_images(self):
        matches = extract_markdown_links(
            "An inline image ![img](https://img.com/image.png) should not match"
        )
        self.assertListEqual([], matches)


if __name__ == "__main__":
    unittest.main()
