from functions.copy_dir import copy_dir
from functions.generate_page import generate_pages_recursive


def main():
    source_dir = "/home/luca/workspace/bootdotdev/10_site_generator/static"
    dest_dir = "/home/luca/workspace/bootdotdev/10_site_generator/public"
    
    print(f"Copying {source_dir} files to {dest_dir}\n")
    try:    
        copy_dir(source_dir, dest_dir)
    except Exception as e:
        raise Exception("copy failed") from e
    
    from_path = "/home/luca/workspace/bootdotdev/10_site_generator/content/"
    template_path = "/home/luca/workspace/bootdotdev/10_site_generator/template.html"
    dest_path = "/home/luca/workspace/bootdotdev/10_site_generator/public/"
    # Change your main function to use generate_pages_recursive instead of generate_page. 
    # You should generate a page for every markdown file in the content directory 
    # and write the results to the public directory.
    generate_pages_recursive(from_path, template_path, dest_path)


main()
