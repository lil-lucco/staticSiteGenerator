from nodes_and_blocks.textnode import TextType, TextNode
from functions.extract_markdown_images import extract_markdown_images


def split_nodes_image(old_nodes):
    # Should behave similarly to split_nodes_delimiter but no delimiter or text type as input
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue

        extracted_images = extract_markdown_images(old_node.text)
        if not extracted_images:
            result.append(old_node)
            continue

        remaining_text = old_node.text

        for alt_text, url in extracted_images:
            image_markdown = f"![{alt_text}]({url})"
            text = remaining_text.split(image_markdown, maxsplit=1)
            if text[0] != "":
                result.append(TextNode(text[0], TextType.TEXT))
            result.append(TextNode(alt_text, TextType.IMAGE, url))

            remaining_text = text[1]

        if remaining_text:
            result.append(TextNode(remaining_text, TextType.TEXT))

    return result
