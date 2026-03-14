import os

# Create nested directories
def create_nested_dirs(path):
    os.makedirs(path, exist_ok=True)
    print("Directories created:", path)


# List files and folders
def list_items(path):
    for item in os.listdir(path):
        print(item)


# Find files by extension
def find_by_extension(path, extension):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                print(os.path.join(root, file))


if __name__ == "__main__":

    create_nested_dirs("example_dir/folder1/folder2")

    print("\nFiles and folders:")
    list_items("example_dir")

    print("\n.txt files:")
    find_by_extension("example_dir", ".txt")