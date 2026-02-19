from nodes_and_blocks.textnode import TextNode
from functions.copy_dir import copy_dir
def main():
    print("Felicitations, Malefactors!")
    test = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(test)
    source_dir = "/home/luca/workspace/bootdotdev/10_site_generator/static"
    dest_dir = "/home/luca/workspace/bootdotdev/10_site_generator/public"
    print(f"Copying {source_dir} files to {dest_dir}")
    try:    
        copy_dir(source_dir, dest_dir)
    except Exception as e:
        raise Exception("copy failed :(") from e
main()
