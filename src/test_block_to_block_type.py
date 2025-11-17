import unittest

from block_to_block_type import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_heading_block(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)

    def test_code_block(self):
        self.assertEqual(block_to_block_type("```python"), BlockType.CODE)

    def test_quote_block(self):
        self.assertEqual(block_to_block_type("> quote"), BlockType.QUOTE)

    def test_unordered_list_block(self):
        self.assertEqual(block_to_block_type("- item"), BlockType.UNORDERED_LIST)

    def test_ordered_list_block(self):
        self.assertEqual(block_to_block_type("12. item"), BlockType.ORDERED_LIST)

    def test_paragraph_block(self):
        self.assertEqual(block_to_block_type("plain paragraph"), BlockType.PARAGRAPH)

    def test_leading_whitespace_is_ignored(self):
        self.assertEqual(block_to_block_type("   - spaced item"), BlockType.UNORDERED_LIST)
