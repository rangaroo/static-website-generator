import os
import shutil

def copy_files_recursive(source, destination):
    source_exists = os.path.exists(f"{source}")
    destination_exists = os.path.exists(f"{destination}")    

    if not source_exists:
        raise Exception("can't access source directory or it does not exist")

    if destination_exists:
        shutil.rmtree(f"{destination}")
        #print(f"{destination} exists, deleting the directory...")

    os.mkdir(f"{destination}")
    #print(f"Created {destination} directory")

    items = os.listdir(source)
    #print(f"Listing the contents of {destination}: {items}")
    #print("----------------------------------------")

    #print(f"Iterating over {source}")
    for item in items:
        new_source = os.path.join(source, item)
        if os.path.isfile(new_source):
            #print(f"{item} is a file. Copying it to {destination} folder")
            shutil.copy(new_source, destination)
            #print(f"File {item} copied to {destination}")
        if os.path.isdir(new_source):
            #print(f"{item} is a directory. Creating a new directory inside {destination} folder")
            new_destination = os.path.join(destination, item)
            #print(f"Subdirectory {item} is created in {destination}")
            #print("******************************")
            copy_files_recursive(new_source, new_destination)
        #print("__________________________________")
