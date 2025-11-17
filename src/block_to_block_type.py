import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(text):
    stripped = text.lstrip()
    match stripped:
        case _ if stripped.startswith("#"):
            return BlockType.HEADING
        case _ if stripped.startswith("```"):
            return BlockType.CODE
        case _ if stripped.startswith(">"):
            return BlockType.QUOTE
        case _ if stripped.startswith("- "):
            return BlockType.UNORDERED_LIST
        case _ if re.match(r"\d+\.", stripped):
            return BlockType.ORDERED_LIST
        case _:
            return BlockType.PARAGRAPH
