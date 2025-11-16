from textnode import TextNode, TextType
from leafnode import LeafNode


def text_node_to_html_node(text_node):
    type = text_node.text_type
    value = text_node.text
    url = text_node.url

    match type:
        case TextType.TEXT:
            return LeafNode(value=value)
        case TextType.BOLD:
            return LeafNode(tag="b", value=value)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=value)
        case TextType.CODE:
            return LeafNode(tag="code", value=value)
        case TextType.LINK:
            return LeafNode(tag="a", value=value, props={"href": url})
        case TextType.IMAGE:
            return LeafNode(tag="img", value="", props={"alt": value, "src": url})
        case _:
            raise ValueError("text node is missing text type")
