import re
from enum import Enum
from htmlnode import HTMLNode

class BlockType(Enum):
    PARAGRAPH = "p"
    HEADING = "h"
    CODE = "code"
    QUOTE = "blockquote"
    UNORDERED_LIST = "ul"
    ORDERED_LIST = "ol"

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        block_type = block_to_block_type(block)
        text = block_to_text(block)

        parent_tag = block_type_to_tag(block_type, block)
        #children = text_to_children(text)

    return

def block_to_text(block):
    block_type = block_to_block_type(block)
    block_one_line = " ".join(block.split("\n"))

    if block_type == BlockType.HEADING:
        text = [re.match(r"(#{1,6})\s(.*)", block_one_line).group(2)]
    elif block_type == BlockType.QUOTE:
        text = [re.match(r">\s(.*)", block_one_line).group(2)]
    elif block_type == BlockType.UNORDERED_LIST or block_type == BlockType.ORDERED_LIST:
        arr = block.split("\n")
        text = []

        unordered = r"-\s(.*)"
        ordered = r"\d+\.\s(.*)"

        pattern = unordered if BlockType.UNORDERED_LIST else ordered

        print(arr, pattern, block_type)
        for string in arr:
            text.append(re.match(pattern, string).group(1))
    else:
        text = [block_one_line]

    return text

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    sections = markdown.split("\n\n")
    arr = []
    for i in range(len(sections)):
        if sections[i] != '':
            arr.append(sections[i].strip())
    return arr

def block_type_to_tag(block):
    block_type = block_to_block_type(block)

    if block_type == BlockType.PARAGRAPH:
        return "p"
    elif block_type == BlockType.QUOTE:
        return "blockquote"
    elif block_type == BlockType.ORDERED_LIST:
        return "ol"
    elif block_type == BlockType.UNORDERED_LIST:
        return "ul"
    elif block_type == BlockType.HEADING:
        if block.startswith("# "):
            return "h1"
        elif block.startswith("## "):
            return "h2"
        elif block.startswith("### "):
            return "h3"
        elif block.startswith("#### "):
            return "h4"
        elif block.startswith("##### "):
            return "h5"
        elif block.startswith("###### "):
            return "h6"

md = "1. This is **bolded** paragraph\n2. text in a p tag here"

print(block_to_text(md))
