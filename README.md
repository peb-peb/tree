# Directory Tree

List contents of directories in tree-like format.

## Installation

## Example

```bash
$ python .\src\tree.py
.\
|
├── src\
│   ├── tree\
│   │   ├── __pycache__\
│   │   │   ├── tree_util.cpython-39.pyc
│   │   │   └── __init__.cpython-39.pyc
│   │   │
│   │   ├── cli.py
│   │   ├── tree_util.py
│   │   └── __init__.py
│   │
│   └── tree.py
│
├── LICENSE
└── README.md
```

## CLI Options

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
