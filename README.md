# Fix space in path

Windows cannot deal with directory names that start or end with a whitespace. When renaming them in Windows Explorer,
spaces are stripped without informing the user. However if other programs create directories with such malformed names,
Windows Explorer cannot delete or rename them anymore. This can happen for example when unpacking a file archive.

This script scans directories recursively, and offers to remove the spaces.

## Dependencies

* [Python 3.8](https://www.python.org/) - Programming language

## Usage
Set the directory you want to scan inside the script, then execute without arguments.

    RECURSIVE_FIX_DIRECTORY_NAMES_HERE = 'C:\\path'

Example output:

     BROKEN: "C:\path\ dir\"
        FIX: "C:\path\dir\"
    Rename this? y
    Fixed.

## Author and license

Copyright © 2020 Miss Mercy  
MIT License
