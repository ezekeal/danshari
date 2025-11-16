from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_images_and_links import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType
from pprint import pprint


def text_to_textnodes(text):
    node = TextNode(text=text, text_type=TextType.TEXT)
    nodes = [node]
    nodes = split_nodes_delimiter(nodes, "**")
    nodes = split_nodes_delimiter(nodes, "`")
    nodes = split_nodes_delimiter(nodes, "_")
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
