from nodes_and_blocks.textnode import TextType, TextNode
from functions.split_nodes_delimiter import split_nodes_delimiter
from functions.split_nodes_image import split_nodes_image
from functions.split_nodes_link import split_nodes_link


def text_to_textnodes(text):
# example input:
# This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)
# example output (list of TextNodes):
# [
#     TextNode("This is ", TextType.TEXT),
#     TextNode("text", TextType.BOLD),
#     TextNode(" with an ", TextType.TEXT),
#     TextNode("italic", TextType.ITALIC),
#     TextNode(" word and a ", TextType.TEXT),
#     TextNode("code block", TextType.CODE),
#     TextNode(" and an ", TextType.TEXT),
#     TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
#     TextNode(" and a ", TextType.TEXT),
#     TextNode("link", TextType.LINK, "https://boot.dev"),
# ]
    if isinstance(text, str):
        nodes = [TextNode(text, TextType.TEXT)]
    elif isinstance(text, list):
        nodes = text
    else:
        raise TypeError("text_to_textnodes expects a str or list of TextNode")

    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
