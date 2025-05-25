import os
import sys
from copy_static import copy_files_recursive
from gencontent import generate_pages_recursive 

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
path_template = "./template.html"
basepath = sys.argv[0]

if basepath == "":
    basepath = "/"

def main():
    copy_files_recursive(dir_path_static, dir_path_public)

    generate_pages_recursive(
        dir_path_content, 
        path_template, 
        dir_path_public,
        basepath
    )

main()
