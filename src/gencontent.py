import os
from block_markdown import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    source_exists = os.path.exists(f"{dir_path_content}")
    if not source_exists:
        raise Exception("can't access source directory or it does not exist")

    items = os.listdir(dir_path_content)
    print(f"Listing the contents of {dest_dir_path}: {items}")
    print("----------------------------------------")
    for item in items:
        new_source_path = os.path.join(dir_path_content, item)
        if os.path.isfile(new_source_path) and os.path.splitext(new_source_path)[-1] == ".md":
            print(f"{item} is a file. Generating a html and copying it to {dest_dir_path} folder")
            generate_page(new_source_path, template_path, os.path.join(dest_dir_path, "index.html"))
            print(f"File {item[:-2]}html is generated inside {dest_dir_path}")
        if os.path.isdir(new_source_path):
            print(f"{item} is a directory. Creating a new directory inside {dest_dir_path} folder")
            new_destination_path = os.path.join(dest_dir_path, item)

            destination_exists = os.path.exists(f"{new_destination_path}")
            if destination_exists:
                shutil.rmtree(f"{new_destination_path}")
                print(f"{new_destination_path} exists, deleting the directory...")
            os.mkdir(f"{new_destination_path}")
            print(f"Subdirectory {item} is created in {dest_dir_path}")
            print("******************************")
            generate_pages_recursive(new_source_path, template_path, new_destination_path)
        print("__________________________________")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as markdown_file:
        markdown = markdown_file.read()

    with open(template_path) as template_file:
        template_html = template_file.read()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    result = template_html.replace("{{ Title }}", title)
    result = result.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as index_html:
        index_html.write(result)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise Exception("could't find the title")
