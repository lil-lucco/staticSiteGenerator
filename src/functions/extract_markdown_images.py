import re


def extract_markdown_images(text):
    # takes raw markdown text and returns a list of tuples
    # each tuple should contain the alt text and the URL of any markdown images
    # example code:
    #
    # text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    # print(extract_markdown_images(text))
    # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
