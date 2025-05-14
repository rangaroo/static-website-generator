import re
from textnode import TextType, TextNode

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        new_node = []
        splitted = old_node.text.split(delimiter)

        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        if len(splitted) % 2 == 0:
            raise ValueError("invalid markdown")

        index = 0
        for item in splitted:
            if item == '':
                index += 1
                continue

            if index % 2 == 0:
                new_node.append(TextNode(item, TextType.TEXT))
            else:
                new_node.append(TextNode(item, text_type))
            index += 1
        
        new_nodes.extend(new_node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        match = extract_markdown_links(node.text)

        if len(match) == 0:
            new_nodes.append(node)
            continue

        splitter(node.text, match, new_nodes, TextType.LINK)

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        match = extract_markdown_images(node.text)

        if len(match) == 0:
            new_nodes.append(node)
            continue

        splitter(node.text, match, new_nodes, TextType.IMAGE)

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def splitter(text, match, arr, text_type):
    # Base case -> when the splitted part is the last section left
    if text == '':
        return

    alt, url = match[0]

    if text_type == TextType.IMAGE:
        sections = text.split(f"![{alt}]({url})", 1)
    else:
        sections = text.split(f"[{alt}]({url})", 1)

    if len(sections) != 2:
        raise ValueError("invalid markdown, image/link section not closed")

    # Case when the text starts with the markdown image/link
    if sections[0] != '':
        arr.append(TextNode(sections[0], TextType.TEXT))
    arr.append(TextNode(alt, text_type, url))

    if len(match) == 1:
        if sections[1] != '':
            arr.append(TextNode(sections[1], TextType.TEXT))
        return
    else:
        splitter(sections[1], match[1:], arr, text_type)
