import unittest

from leafnode import LeafNode

example_url = "https://www.example.com"


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Link", props={"href": example_url})
        self.assertEqual(node.to_html(), f'<a href="{example_url}">Link</a>')
