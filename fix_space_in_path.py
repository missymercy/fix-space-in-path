import os

RECURSIVE_FIX_DIRECTORY_NAMES_HERE = 'C:\\path'
MAX_DIRECTORY_LENGTH = 255
MAX_FILENAME_LENGTH = 143


def main() -> None:
    for root, directories, files in os.walk(RECURSIVE_FIX_DIRECTORY_NAMES_HERE):
        for directory in directories:
            rename(broken=os.path.join(root, directory) + os.sep,
                   fixed=os.path.join(root, fix_dir(directory)) + os.sep)
        for file in files:
            rename(broken=os.path.join(root, file),
                   fixed=os.path.join(root, fix_file(file)))


def fix_file(
        name: str
) -> str:
    # fix filename characters
    name, extension = os.path.splitext(name)
    name = name.lstrip(' ').rstrip(' .')
    # fix filename length
    extension = extension.strip(' ')
    max_length = MAX_FILENAME_LENGTH - len(extension)
    name = name[:max_length]
    # fix filename characters again
    name = name.lstrip(' ').rstrip(' .')
    # done
    return name + extension


def fix_dir(
        name: str
) -> str:
    return name.strip(' ')[:MAX_DIRECTORY_LENGTH]


def rename(
        broken: str,
        fixed: str
) -> None:
    if broken == fixed:
        return
    print(f' BROKEN: "{broken}"\n    FIX: "{fixed}"')
    if os.path.exists(fixed):
        print('Cannot fix, target already exists.')
    elif input('Rename this? ') == 'y':
        os.rename(broken, fixed)
        print('Fixed.\n')
    else:
        print('Not fixed.\n')


if __name__ == '__main__':
    main()
