import os
import shutil


def copy_static_files(static_dir="static", public_dir="docs"):
    if not os.path.exists(static_dir):
        os.exit(1)
    os.makedirs(public_dir)
    copy_folder(static_dir, public_dir)


def copy_folder(from_path, to_path):
    dir_list = os.listdir(from_path)
    files = list(filter(lambda x: os.path.isfile(f"{from_path}/{x}"), dir_list))
    dirs = list(filter(lambda x: os.path.isdir(f"{from_path}/{x}"), dir_list))
    for file in files:
        shutil.copy(f"{from_path}/{file}", to_path)

    for dir in dirs:
        new_from_path = f"{from_path}/{dir}"
        new_to_path = f"{to_path}/{dir}"
        if not os.path.exists(new_to_path):
            os.mkdir(new_to_path)
        copy_folder(new_from_path, new_to_path)
