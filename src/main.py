from textnode import TextNode, TextType
from copy_static_files import copy_static_files
from generate_page import generate_page
import os
import shutil


def main():
    public_dir = "public"
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    copy_static_files()
    generate_page("content/index.md", "template.html", "public/index.html")


main()
