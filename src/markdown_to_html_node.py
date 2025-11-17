from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from text_to_textnodes import text_to_textnodes
from text_node_to_html import text_node_to_html_node
from leafnode import LeafNode
from parentnode import ParentNode


def _inline_text_to_html_nodes(text):
    nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in nodes]


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
            html_nodes = _inline_text_to_html_nodes(text.replace("\n", " "))
            return ParentNode(tag="p", children=html_nodes)
        case BlockType.HEADING:
            hash_count = len(text.split(" ")[0])
            if hash_count > 6:
                hash_count = 6
            tag = f"h{hash_count}"
            heading_text = text[hash_count:].strip()
            html_nodes = _inline_text_to_html_nodes(heading_text)
            return ParentNode(tag=tag, children=html_nodes)
        case BlockType.CODE:
            code_text = text.replace("```", "").lstrip("\n")
            code_node = LeafNode(code_text, tag="code")
            return ParentNode(tag="pre", children=[code_node])
        case BlockType.QUOTE:
            lines = []
            for line in text.split("\n"):
                lines.append(line.lstrip("> ").rstrip())
            quote_text = "\n".join(lines).strip()
            html_nodes = _inline_text_to_html_nodes(quote_text)
            return ParentNode(tag="blockquote", children=html_nodes)
        case BlockType.UNORDERED_LIST:
            items = []
            for line in text.split("\n"):
                stripped = line.strip()
                if not stripped:
                    continue
                item_text = stripped[2:] if len(stripped) > 2 else ""
                html_nodes = _inline_text_to_html_nodes(item_text)
                items.append(ParentNode(tag="li", children=html_nodes))
            return ParentNode(tag="ul", children=items)
        case BlockType.ORDERED_LIST:
            items = []
            for line in text.split("\n"):
                stripped = line.strip()
                if not stripped:
                    continue
                if "." in stripped:
                    item_text = stripped.split(".", 1)[1].strip()
                else:
                    item_text = stripped
                html_nodes = _inline_text_to_html_nodes(item_text)
                items.append(ParentNode(tag="li", children=html_nodes))
            return ParentNode(tag="ol", children=items)
