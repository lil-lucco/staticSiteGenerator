import os
from functions.markdown_to_html_node import markdown_to_html_node
from functions.extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as t:    
        template = t.read()
    
    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    final_html = template.replace("{{ Content }}", html_string)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as d:
        chars_written = d.write(final_html)
    print(f"SUCCESS!\n{chars_written} characters written to {dest_path}.")
