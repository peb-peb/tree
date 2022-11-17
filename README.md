# Directory Tree

List contents of directories in tree-like format.



## Installation

To install `tree`, just run the following command:

```zsh
pip install tree-peb
```

**NOTE**: Ensure that you have python 3.7 or greater installed on your machine to run this on your system.

## Project Structure

```text
$ python3 .\tree.py
.\
|
├── tree\
│   ├── __init__.py
│   ├── cli.py
│   └── tree_util.py
│
├── LICENSE
├── README.md
└── tree.py
```

`tree.py` is the starting point for the script.

`cli.py` contains all the command line arguments.

`tree_util.py` contains all the utilities for fetching and displaying the tree diagram of directory.

## CLI Options

If you run `tree` with a directory path as an argument, then you get a full directory tree printed on your screen. The default input directory is your current directory.

```text
usage: tree [-h] [-v] [-d] [-o OUTPUT_FILE] [ROOT_DIR]

positional arguments:
  ROOT_DIR              Generate a full directory tree from the given ROOT_DIR

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -d, --dir-only        Generate a directory-only tree
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        Store the tree output in a file
```
