from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from text_to_textnodes import text_to_textnodes
from text_node_to_html import text_node_to_html_node
from leafnode import LeafNode
from parentnode import ParentNode


def markdown_to_html_node(text):
    html_children = []
    blocks = markdown_to_blocks(text)
    for block in blocks:
        children = text_to_children(block)
        html_children.append(children)
    parent_node = ParentNode(tag="div", children=html_children)
    return parent_node


def text_to_children(text):
    type = block_to_block_type(text)
    match type:
        case BlockType.PARAGRAPH:
            nodes = text_to_textnodes(text.replace("\n", " "))
            html_nodes = list(map(text_node_to_html_node, nodes))
            return ParentNode(tag="p", children=html_nodes)
        case BlockType.HEADING:
            hash_count = len(text.split(" ")[0])
            if hash_count > 6:
                hash_count = 6
            tag = f"h{hash_count}"
            heading_text = text.replace("#", "")
            return LeafNode(heading_text, tag=tag)
        case BlockType.CODE:
            code_text = text.replace("```", "").lstrip("\n")
            code_node = LeafNode(code_text, tag="code")
            return ParentNode(tag="pre", children=[code_node])
        case BlockType.QUOTE:
            code_text = text.replace(">", "")
            return LeafNode(code_text, tag="blockquote")
        case BlockType.UNORDERED_LIST:
            lines = text.split("\n")
            lines = list(lambda x: LeafNode(x.strip().slice[2:], tag="li"), lines)
            return ParentNode(tag="ul", children=lines)
        case BlockType.ORDERED_LIST:
            lines = text.split("\n")
            lines = list(lambda x: LeafNode(x.split(".".strip(), tag="ul")), lines)
            return ParentNode(tag="ol", children=lines)
