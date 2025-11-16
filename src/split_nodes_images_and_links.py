from extract_markdown_images_and_links import (
    extract_markdown_images,
    extract_markdown_links,
)
from textnode import TextNode, TextType


def split_nodes_image(old_nodes):
    nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        if len(images) == 0:
            nodes.append(old_node)
            continue
        remaining_text = old_node.text
        for alt, url in images:
            image_text = f"![{alt}]({url})"
            parts = remaining_text.split(image_text, 1)
            if len(parts) != 2:
                raise ValueError("Image markdown parsing failed")
            text_before, remaining_text = parts
            if len(text_before) > 0:
                nodes.append(TextNode(text=text_before, text_type=TextType.TEXT))
            nodes.append(TextNode(text=alt, text_type=TextType.IMAGE, url=url))
        if len(remaining_text) > 0:
            nodes.append(TextNode(text=remaining_text, text_type=TextType.TEXT))
    return nodes


def split_nodes_link(old_nodes):
    nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        if len(links) == 0:
            nodes.append(old_node)
            continue
        remaining_text = old_node.text
        for alt, url in links:
            link_text = f"[{alt}]({url})"
            parts = remaining_text.split(link_text, 1)
            if len(parts) != 2:
                raise ValueError("Link markdown parsing failed")
            text_before, remaining_text = parts
            if len(text_before) > 0:
                nodes.append(TextNode(text=text_before, text_type=TextType.TEXT))
            nodes.append(TextNode(text=alt, text_type=TextType.LINK, url=url))
        if len(remaining_text) > 0:
            nodes.append(TextNode(text=remaining_text, text_type=TextType.TEXT))
    return nodes
