from copy_static_files import copy_static_files
from generate_pages_recursively import generate_pages_recursively
import os
import shutil
import sys


def main():
    basepath = "/" if len(sys.argv) < 2 else sys.argv[1]
    print(basepath)
    static_dir = "static"
    public_dir = "docs"
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    copy_static_files(static_dir=static_dir, public_dir=public_dir)
    generate_pages_recursively("content", "template.html", public_dir, basepath)


main()
