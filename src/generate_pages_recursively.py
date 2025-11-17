import os
from generate_page import generate_page


def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dir_path_content):
        raise ValueError("contant path does not exist")
    if not os.path.exists(dest_dir_path):
        raise ValueError("destination path does not exist")
    if not os.path.exists(template_path):
        raise ValueError("template path does not exist")
    generate_files_in_dir(dir_path_content, template_path, dest_dir_path)


def generate_files_in_dir(dir_path_content, template_path, dest_dir_path):
    dir_list = os.listdir(dir_path_content)
    files = list(filter(lambda x: os.path.isfile(f"{dir_path_content}/{x}"), dir_list))
    dirs = list(filter(lambda x: os.path.isdir(f"{dir_path_content}/{x}"), dir_list))
    for file in files:
        filename, _ = os.path.splitext(file)
        generate_page(
            f"{dir_path_content}/{file}",
            template_path,
            f"{dest_dir_path}/{filename}.html",
        )
    for dir in dirs:
        new_content_path = f"{dir_path_content}/{dir}"
        new_dest_path = f"{dest_dir_path}/{dir}"
        generate_files_in_dir(new_content_path, template_path, new_dest_path)
