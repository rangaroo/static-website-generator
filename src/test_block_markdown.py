import unittest
from textnode import TextType, TextNode
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class TestBlockTypes(unittest.TestCase):
    def test_block_types(self):
        md = """
# Hello

This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items

1. This is a
2. Ordered list

1. This is
3. not a ordered list

```
this is a code block
```

> this is quote
"""
        blocks = markdown_to_blocks(md)
        block_types = []
        for block in blocks:
            block_types.append(block_to_block_type(block))

        self.assertListEqual(
            block_types,
            [
                BlockType.HEADING,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
                BlockType.UNORDERED_LIST,
                BlockType.ORDERED_LIST,
                BlockType.PARAGRAPH,
                BlockType.CODE,
                BlockType.QUOTE
            ],
        )
if __name__ == "__main__":
    unittest.main()
