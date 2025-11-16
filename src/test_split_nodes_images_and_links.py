import unittest

from split_nodes_images_and_links import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


class TestSplitNodesImagesAndLinks(unittest.TestCase):
    def test_split_nodes_image_single(self):
        node = TextNode(
            "This is text with ![alt text](https://example.com/img.png) afterwards",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("alt text", TextType.IMAGE, "https://example.com/img.png"),
                TextNode(" afterwards", TextType.TEXT),
            ],
        )

    def test_split_nodes_link_multiple(self):
        node = TextNode(
            "Links: [One](https://one.com) and [Two](https://two.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("Links: ", TextType.TEXT),
                TextNode("One", TextType.LINK, "https://one.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("Two", TextType.LINK, "https://two.com"),
            ],
        )

    def test_split_ignores_non_text(self):
        node = TextNode("![alt](https://img.com/img.png)", TextType.IMAGE)
        self.assertEqual(split_nodes_image([node]), [node])
        link_node = TextNode("[link](https://example.com)", TextType.LINK, None)
        self.assertEqual(split_nodes_link([link_node]), [link_node])


if __name__ == "__main__":
    unittest.main()
