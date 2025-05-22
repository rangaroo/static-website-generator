import os
from markdown_blocks import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as markdown_file:
        markdown = markdown_file.read()

    with open(template_path) as template_file:
        template_html = template_file.read()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    result = template_html.replace("{{ Title }}", title)
    result = result.replace("{{ Content }}", content)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as index_html:
        index_html.write(html_final)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# ")
            return line[2:]
    raise Exception("could't find the title")
