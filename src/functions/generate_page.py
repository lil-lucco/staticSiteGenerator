from pathlib import Path
from functions.markdown_to_html_node import markdown_to_html_node
from functions.extract_title import extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    from_path = Path(from_path)
    template_path = Path(template_path)
    dest_path = Path(dest_path)

    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")
    with from_path.open(encoding="utf-8") as f:
        markdown = f.read()
    with template_path.open(encoding="utf-8") as t:
        template = t.read()
    
    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    final_html = template.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_string)
    final_html = final_html.replace('href="/', f'href="{basepath}')
    final_html = final_html.replace('src="/', f'src="{basepath}')

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    with dest_path.open("w", encoding="utf-8") as d:
        chars_written = d.write(final_html)
    print(f"SUCCESS!\n{chars_written} characters written to {dest_path}.")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    dir_path_content = Path(dir_path_content)
    dest_dir_path = Path(dest_dir_path)

    # Crawl every entry in the current content directory.
    for source_path in dir_path_content.iterdir():
        dest_path = dest_dir_path / source_path.name

        # Recurse into directories so we preserve the same structure in the output dir.
        if source_path.is_dir():
            generate_pages_recursive(source_path, template_path, dest_path, basepath)
            continue

        # Convert markdown files to html files.
        if source_path.is_file() and source_path.suffix == ".md":
            html_dest_path = dest_path.with_suffix(".html")
            generate_page(source_path, template_path, html_dest_path, basepath)
            
        
