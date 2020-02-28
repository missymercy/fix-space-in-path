import os

RECURSIVE_FIX_DIRECTORY_NAMES_HERE = 'C:\\path'


def main() -> None:
    for root, directories, files in os.walk(RECURSIVE_FIX_DIRECTORY_NAMES_HERE):
        for directory in directories:
            if not (directory.startswith(' ') or directory.endswith(' ')):
                continue
            broken = os.path.join(root, directory) + os.sep
            fixed = os.path.join(root, directory.strip(' ')) + os.sep
            print(f' BROKEN: "{broken}"\n    FIX: "{fixed}"')
            if input('Rename this? ') == 'y':
                os.rename(broken, fixed)
                print('Fixed.\n')
            else:
                print('Not fixed.\n')


if __name__ == '__main__':
    main()
