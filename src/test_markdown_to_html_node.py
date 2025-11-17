import unittest
from textwrap import dedent

from markdown_to_html_node import markdown_to_html_node, text_to_children


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = dedent(
            """
            This is **bolded** paragraph
            text in a p
            tag here

            This is another paragraph with _italic_ text and `code` here

            """
        )

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p>"
            "<p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = dedent(
            """
            ```
            This is text that _should_ remain
            the **same** even with inline stuff
            ```
            """
        )

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\n"
            "the **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading_block(self):
        node = markdown_to_html_node("# Heading")
        self.assertEqual(node.to_html(), "<div><h1>Heading</h1></div>")

    def test_quote_block(self):
        md = dedent(
            """
            > Quote line 1
            > Quote line 2
            """
        )
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><blockquote>Quote line 1\nQuote line 2</blockquote></div>",
        )

    def test_list_with_links(self):
        md = dedent(
            """
            - [First](https://example.com/1)
            - Item with **bold**
            """
        )
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><ul><li><a href=\"https://example.com/1\">First</a></li>"
            "<li>Item with <b>bold</b></li></ul></div>",
        )


class TestTextToChildren(unittest.TestCase):
    def test_heading_child(self):
        node = text_to_children("### Heading text")
        self.assertEqual(node.to_html(), "<h3>Heading text</h3>")

    def test_quote_child(self):
        node = text_to_children("> quoted content")
        self.assertEqual(node.to_html(), "<blockquote>quoted content</blockquote>")

    def test_code_child(self):
        node = text_to_children("```\nline one\nline two\n```")
        self.assertEqual(
            node.to_html(),
            "<pre><code>line one\nline two\n</code></pre>",
        )


if __name__ == "__main__":
    unittest.main()
