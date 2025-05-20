import os
import shutil

def generate_public(source='static', destination='public'):
    source_exists = os.path.exists(f"{source}")
    destination_exists = os.path.exists(f"{destination}")    

    if not source_exists:
        raise Exception("can't access source directory or it does not exist")

    if destination_exists:
        shutil.rmtree(f"{destination}")

    os.mkdir(f"{destination}")

    items = os.listdir(source)
    for item in items:
        new
        if os.path.isfile(item):
            print(f"File: {item}")
        if os.path.isdir(item):
            generate_public()
            print(f"Subdirectory: {item}")
