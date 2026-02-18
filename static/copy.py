import os
import shutil

def copy(source, dest):
# a recursive function that copies all the contents from a source directory to a destination directory (in our case, static to public)
    if not os.path.exists(dest): # check if it exists
        os.mkdir(dest)
    else: #  It should first delete all the contents of the destination directory (public) to ensure that the copy is clean.
        shutil.rmtree(dest)
        os.mkdir(dest)
#     It should copy all files and subdirectories, nested files, etc.
    items_to_copy = os.listdir(source)
    for item_path in items_to_copy:
        if os.path.isfile(item_path):
            shutil.copy(item_path, dest)
            copy(item_path, dest)
        else:
            copy(item_path, dest)
            ## add "item_path\n" to log.md

#     I recommend logging the path of each file you copy, so you can see what's happening as you run and debug your code.
