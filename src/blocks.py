from functions import *
from enum import Enum

def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")
    blocks = []
    for block in raw_blocks:
        stripped = block.strip()
        if stripped != "":
            blocks.append(stripped)
    return blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(text):
    # Takes a single block of markdown text as input and returns the BlockType representing the type of block it is
    # Assume all leading and trailing whitespace were already stripped (we did that in markdown_to_blocks())
    headings = [
        "# ",
        "## ",
        "### ",
        "#### ",
        "##### ",
        "###### ",
    ]
    if any(text.startswith(prefix) for prefix in headings):
        return BlockType.HEADING
    if text.startswith("```\n") and text.endswith("```"):
        return BlockType.CODE
    if text.startswith(">"):
        return BlockType.QUOTE
    if text.startswith("- "):
        return BlockType.UNORDERED_LIST
    if text.startswith("1. "):
        parts = text.split("\n")
        for i, part in enumerate(parts, start=1):
            if not part.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
            
            

    
