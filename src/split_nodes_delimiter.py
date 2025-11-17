from textnode import TextNode, TextType

delimiter_type_map = {
    "`": TextType.CODE,
    "**": TextType.BOLD,
    "_": TextType.ITALIC,
}


def split_nodes_delimiter(old_nodes, delimiter):
    nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT or delimiter not in old_node.text:
            nodes.append(old_node)
            continue
        chunks = old_node.text.split(delimiter)
        for i, text in enumerate(chunks):
            if len(text) == 0:
                continue
            is_delimited = i % 2 == 1
            text_type = delimiter_type_map[delimiter] if is_delimited else TextType.TEXT
            nodes.append(TextNode(text, text_type=text_type))
    return nodes
