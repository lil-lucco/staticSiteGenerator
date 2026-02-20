from functions.copy_dir import copy_dir
from functions.generate_page import generate_page


def main():
    source_dir = "/home/luca/workspace/bootdotdev/10_site_generator/static"
    dest_dir = "/home/luca/workspace/bootdotdev/10_site_generator/public"
    
    print(f"Copying {source_dir} files to {dest_dir}")
    try:    
        copy_dir(source_dir, dest_dir)
    except Exception as e:
        raise Exception("copy failed") from e
    
    from_path = "/home/luca/workspace/bootdotdev/10_site_generator/content/index.md"
    template_path = "/home/luca/workspace/bootdotdev/10_site_generator/template.html"
    dest_path = "/home/luca/workspace/bootdotdev/10_site_generator/public/index.html"
    generate_page(from_path, template_path, dest_path)


main()
