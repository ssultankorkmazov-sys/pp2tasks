import os

# Copy file without shutil
def copy_file(src, dst):
    with open(src, "rb") as f1:
        data = f1.read()

    with open(dst, "wb") as f2:
        f2.write(data)

    print("File copied")


# Move file (copy + delete)
def move_file(src, dst):
    copy_file(src, dst)
    os.remove(src)
    print("File moved")


if __name__ == "__main__":

    src = "example_dir/test.txt"
    dst_copy = "example_dir/copy_test.txt"
    dst_move = "example_dir/moved_test.txt"

    if os.path.exists(src):
        copy_file(src, dst_copy)
        move_file(src, dst_move)
    else:
        print("Source file not found")