from copy_static_files import copy_static_files
from generate_pages_recursively import generate_pages_recursively
import os
import shutil


def main():
    public_dir = "public"
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    copy_static_files()
    generate_pages_recursively("content", "template.html", "public")


main()
