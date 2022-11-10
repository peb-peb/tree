import argparse
import pathlib
import sys

from .tree_util import DirectoryTree

VERSION = "v0.1.0"

def parse_arguments():
    parser = argparse.ArgumentParser(prog="tree")
    parser.version = f"Tree {VERSION}"
    parser.add_argument(
        "root_dir",
        metavar="ROOT_DIR",
        nargs="?",
        default=".",
        help="Generate a full directory tree from the given ROOT_DIR",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
    )
    parser.add_argument(
        "-d",
        "--dir-only",
        action="store_true",
        default=False,
        help="Generate a directory-only tree",
    )
    parser.add_argument(
        "-o",
        "--output-file",
        default=sys.stdout,
        help="Store the tree output in a file",
    )
    return parser.parse_args()

def main():
    args = parse_arguments()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("The Specified root directory doesn't exist or is a file")
        sys.exit()
    tree = DirectoryTree(root_dir, dir_only=args.dir_only, output_file=args.output_file)
    tree.generate()
