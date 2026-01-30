from textnode import TextType, TextNode
from leafnode import LeafNode

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

def split_nodes_delimiter(old_nodes, delimeter, text_type):
    pass #