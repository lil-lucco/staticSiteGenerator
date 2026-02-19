from nodes_and_blocks.textnode import TextType, TextNode
from nodes_and_blocks.parentnode import ParentNode
from nodes_and_blocks.block_type import BlockType
from nodes_and_blocks.markdown_to_blocks import markdown_to_blocks
from nodes_and_blocks.block_to_block_type import block_to_block_type
from functions.text_to_textnodes import text_to_textnodes
from functions.text_node_to_html_node import text_node_to_html_node


def markdown_to_html_node(markdown):
# Converts a full markdown document into a single parent HTMLNode.
# That one parent HTMLNode should (obviously) contain many child HTMLNode objects representing the nested elements.


    blocks = markdown_to_blocks(markdown)
    parent_children = []
    for block in blocks:
        blocktype = block_to_block_type(block)
# Quote blocks should be surrounded by a <blockquote> tag.
        if blocktype == BlockType.QUOTE:
            parts = block.split("\n")
            cleaned_text_lines = []
            for part in parts:
                if part == "":
                    continue
                clean_text = part[1:]
                clean_text = clean_text.lstrip()
                cleaned_text_lines.append(clean_text)
            cleaned_joined_text = " ".join(cleaned_text_lines)
            block_children = inline_text_to_children(cleaned_joined_text)
            parent_children.append(ParentNode("blockquote", block_children))
# Unordered list blocks should be surrounded by a <ul> tag, and each list item should be surrounded by a <li> tag.
        elif blocktype == BlockType.UNORDERED_LIST:
            parts = block.split("\n")
            block_children = []
            for part in parts:
                clean_text = part[1:]
                clean_text = clean_text.lstrip()
                clean_text = inline_text_to_children(clean_text)
                block_children.append(ParentNode("li", clean_text))
            parent_children.append(ParentNode("ul", block_children))
# Ordered list blocks should be surrounded by a <ol> tag, and each list item should be surrounded by a <li> tag.
# For UNORDERED_LIST and ORDERED_LIST, you're currently treating the entire block as one set of children.
# However, the instructions say that each list item should be surrounded by a <li> tag.
# How might you split that block into individual lines and wrap each line in its own ParentNode("li", ...)
# before putting them inside the <ul> or <ol>?
        elif blocktype == BlockType.ORDERED_LIST:
            parts = block.split("\n")
            block_children = []
            for i, part in enumerate(parts):
                content = part.split(".", 1)
                clean_text = inline_text_to_children(content[1].lstrip())
                block_children.append(ParentNode("li", clean_text))
            parent_children.append(ParentNode("ol", block_children))
# Code blocks should be surrounded by a <code> tag nested inside a <pre> tag.
        elif blocktype == BlockType.CODE:
            code_text_parts = block.split("\n")
            clean_lines = [ln.lstrip() for ln in code_text_parts]
            code_text = "\n".join(clean_lines[1:-1]) + "\n"
            code_htmlnode = text_node_to_html_node(TextNode(code_text, TextType.TEXT))
            inner_node = ParentNode("code", [code_htmlnode])
            parent_children.append(ParentNode("pre", [inner_node]))
# Headings should be surrounded by a <h1> to <h6> tag, depending on the number of # characters.
        elif blocktype == BlockType.HEADING:
            n = 0
            while n < len(block) and block[n] == "#":
                n += 1
            block_children = inline_text_to_children(block[n:].lstrip())
            parent_children.append(ParentNode(f"h{min(n, 6)}", block_children))
# Paragraphs should be surrounded by a <p> tag. I removed the newlines and replaced them with spaces.
        elif blocktype == BlockType.PARAGRAPH:
            lines = block.split("\n")
            clean_lines = [ln.lstrip() for ln in lines]
            text = " ".join(clean_lines)
            block_children = inline_text_to_children(text)
            parent_children.append(ParentNode("p", block_children))

    return ParentNode("div", parent_children)


def inline_text_to_children(block):
# For paragraph/heading/list items/quote you should:
#     turn the block's text into TextNodes (your text_to_textnodes)
#     then convert each TextNode to an HTML node (text_node_to_html_node)
#     that list becomes the children of the block ParentNode
    textnodes = text_to_textnodes(block)
    children = []
    for node in textnodes:
        children.append(text_node_to_html_node(node))
    return children
