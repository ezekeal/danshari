from textnode import TextNode, TextType

delimiter_type_map = {
    "`": TextType.CODE,
    "**": TextType.BOLD,
    "_": TextType.ITALIC,
}


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT or delimiter not in old_node.text:
            nodes.append(old_node)
            continue
        starts_with_delimiter = old_node.text[0] == delimiter
        chunks = old_node.text.split(delimiter)
        for i in range(len(chunks)):
            text = chunks[i]
            if len(text) == 0:
                continue
            is_even = i % 2 == 0
            is_delimited = (
                starts_with_delimiter
                and is_even
                or (not starts_with_delimiter and not is_even)
            )
            type = delimiter_type_map[delimiter] if is_delimited else TextType.TEXT
            node = TextNode(text, text_type=type)
            nodes.append(node)
    return nodes
