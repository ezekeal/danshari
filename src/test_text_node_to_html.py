import unittest

from textnode import TextNode, TextType
from text_node_to_html import text_node_to_html_node


class TestTextNodeToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode(text="This is a text node", text_type=TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode(text="bold text", text_type=TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "bold text")

    def test_italic(self):
        node = TextNode(text="italic text", text_type=TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "italic text")

    def test_code(self):
        node = TextNode(text="print('hello')", text_type=TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('hello')")

    def test_link(self):
        node = TextNode(
            text="click me", text_type=TextType.LINK, url="https://boot.dev"
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "https://boot.dev"})
        self.assertEqual(html_node.value, "click me")

    def test_image(self):
        node = TextNode(
            text="A cat", text_type=TextType.IMAGE, url="https://example.com/cat.png"
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(
            html_node.props,
            {"alt": "A cat", "src": "https://example.com/cat.png"},
        )
        self.assertEqual(html_node.value, "")

    def test_unknown_type_raises(self):
        node = TextNode(text="oops", text_type="unknown")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)
