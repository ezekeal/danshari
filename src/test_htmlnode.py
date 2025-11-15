import unittest

from htmlnode import HTMLNode

example_url = "https://www.example.com"


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": example_url, "target": "_blank"})
        self.assertEqual(node.props_to_html(), f' href="{example_url}" target="_blank"')

    def test_props_to_html_without_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode("p", props={"href": example_url})
        self.assertEqual(
            repr(node),
            f"tag: p value: None children: None props: {{'href': '{example_url}'}}",
        )
