import unittest

from textnode import TextNode, TextType

example_url = "https://www.example.com"


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode(text="This is a text node", text_type=TextType.BOLD)
        node2 = TextNode(text="This is a text node", text_type=TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode(text="This is a text node", text_type=TextType.BOLD)
        node2 = TextNode(text="This is a text node", text_type=TextType.TEXT)
        node3 = TextNode(
            text="This is a text node", text_type=TextType.TEXT, url=example_url
        )
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node2, node3)

    def test_repr(self):
        node = TextNode(
            text="This is a text node", text_type=TextType.TEXT, url=example_url
        )
        self.assertEqual(
            repr(node),
            "TextNode(This is a text node, TextType.TEXT, https://www.example.com)",
        )


if __name__ == "__main__":
    unittest.main()
