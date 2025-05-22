from copy_static import copy_files_recursive
from gencontent import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
path_template = "./template.html"

def main():
    copy_files_recursive(dir_path_static, dir_path_public)

    generate_page(
        os.path.join(dir_path_content, "index.md"), 
        path_template, 
        os.path.join(dir_path_public, "index.html"),
    )

main()
