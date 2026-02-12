from textnode import TextType, TextNode
from leafnode import LeafNode
import re

def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise TypeError
    else:
        match text_node.text_type:
            case TextType.TEXT:
                return LeafNode(None, text_node.text)
            case TextType.BOLD:
                return LeafNode("b", text_node.text)
            case TextType.ITALIC:
                return LeafNode("i", text_node.text)
            case TextType.CODE:
                return LeafNode("code", text_node.text)
            case TextType.LINK:
                return LeafNode("a", text_node.text, text_node.prop["href"])
            case TextType.IMAGE:
                return LeafNode("img", "", text_node.prop["src"])

def split_nodes_delimiter(old_nodes, delimiter, text_type):

# It takes a list of "old nodes", a delimiter, and a text type. It should return a new list of nodes, 
# where any "text" type nodes in the input list are (potentially) split into multiple nodes based on the syntax. 
# For example, given the following input:
#   ``` node = TextNode("This is text with a `code block` word", TextType.TEXT)
#       new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)```
# `new_nodes` becomes:
#   ```[
#          TextNode("This is text with a ", TextType.TEXT),
#          TextNode("code block", TextType.CODE),
#          TextNode(" word", TextType.TEXT),
#      ]```

    # Build a brand-new list rather than mutating the input list.
    result = []

    for old_node in old_nodes:
        # Only raw text nodes can be split further. Already-formatted nodes pass through.
        # This keeps nested parsing steps composable (text -> code -> bold -> italics).
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue

        # Splitting on a delimiter should alternate as:
        # plain, formatted, plain, formatted, plain, ...
        # If we get an even number of parts, the markdown is unbalanced.
        parts = old_node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError(f"invalid markdown syntax: missing closing '{delimiter}'")

        # Even indexes are plain text, odd indexes are wrapped in `text_type`.
        for i, part in enumerate(parts):
            # Skip empty chunks so we don't emit empty TextNodes.
            if part == "":
                continue
            if i % 2 == 0:
                result.append(TextNode(part, TextType.TEXT))
            else:
                result.append(TextNode(part, text_type))

    return result

def extract_markdown_images(text):
    # takes raw markdown text and returns a list of tuples
    # each tuple should contain the alt text and the URL of any markdown images
    # example code:
    # 
    # text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    # print(extract_markdown_images(text))        
    # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    pass

def extract_markdown_links(text):
    # same as above but with HUYAHH
    # example code:
    #
    # text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    # print(extract_markdown_links(text))
    # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
    pass