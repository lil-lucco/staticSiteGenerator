from nodes_and_blocks.textnode import TextType, TextNode
from functions.extract_markdown_links import extract_markdown_links


def split_nodes_link(old_nodes):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue

        extracted_links = extract_markdown_links(old_node.text)
        if not extracted_links:
            result.append(old_node)
            continue

        remaining_text = old_node.text

        for alt_text, url in extracted_links:
            text_markdown = f"[{alt_text}]({url})"
            text = remaining_text.split(text_markdown, maxsplit=1)
            if text[0] != "":
                result.append(TextNode(text[0], TextType.TEXT))
            result.append(TextNode(alt_text, TextType.LINK, url))

            remaining_text = text[1]

        if remaining_text:
            result.append(TextNode(remaining_text, TextType.TEXT))

    return result
