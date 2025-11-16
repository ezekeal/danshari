import unittest

from parentnode import ParentNode
from leafnode import LeafNode

example_url = "https://www.example.com"


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode(tag="span", value="child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode(tag="b", value="grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_multiple_children(self):
        children = [
            LeafNode(tag="span", value="first"),
            LeafNode(tag="span", value="second"),
        ]
        parent_node = ParentNode("div", children)
        self.assertEqual(parent_node.to_html(), "<div><span>first</span><span>second</span></div>")

    def test_parent_node_requires_tag(self):
        child_node = LeafNode(tag="span", value="child")
        with self.assertRaises(ValueError):
            ParentNode(None, [child_node])

    def test_parent_node_requires_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)

    def test_parent_node_renders_props(self):
        child_node = LeafNode(tag="span", value="child")
        parent_node = ParentNode("div", [child_node], props={"class": "wrapper"})
        self.assertEqual(parent_node.to_html(), '<div class="wrapper"><span>child</span></div>')
