from functions.copy_dir import copy_dir
from functions.generate_page import generate_pages_recursive
import sys
from pathlib import Path


def main():
    project_root = Path(__file__).resolve().parents[1]
    source_dir = project_root / "static"
    dest_dir = project_root / "docs"
    
    print(f"Copying {source_dir} files to {dest_dir}\n")
    try:    
        copy_dir(source_dir, dest_dir)
    except Exception as e:
        raise Exception("copy failed") from e
    
    from_path = project_root / "content"
    template_path = project_root / "template.html"
    dest_path = project_root / "docs"

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    if not basepath.startswith("/"):
        basepath = f"/{basepath}"
    if basepath != "/" and not basepath.endswith("/"):
        basepath = f"{basepath}/"

    generate_pages_recursive(from_path, template_path, dest_path, basepath)


if __name__ == "__main__":
    main()
