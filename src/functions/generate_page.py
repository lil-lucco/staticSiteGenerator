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

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Crawl every entry in the current content directory.
    for entry in os.listdir(dir_path_content):
        source_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        # Recurse into directories so we preserve the same structure in /public.
        if os.path.isdir(source_path):
            generate_pages_recursive(source_path, template_path, dest_path)
            continue

        # Convert markdown files to html files.
        if os.path.isfile(source_path) and entry.endswith(".md"):
            html_dest_path = os.path.splitext(dest_path)[0] + ".html"
            generate_page(source_path, template_path, html_dest_path)
            
# Run the new program and ensure that both pages on the site are generated correctly and you can navigate between them.
