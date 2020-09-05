import os
from typing import Iterable


class NameFix(object):
    def __init__(
            self,
            root_directory: str,
            exclude: Iterable[str],
            max_directory_length: int,
            max_filename_length: int
    ) -> None:
        self.root_directory = root_directory
        exclude = [os.path.abspath(os.path.join(self.root_directory, entry)) for entry in exclude]
        self.exclude_dirs = [entry for entry in exclude if os.path.isdir(entry)]
        self.exclude_files = [entry for entry in exclude if os.path.isfile(entry)]
        self.max_directory_length = max_directory_length
        self.max_filename_length = max_filename_length

    def run(self) -> None:
        for root, directories, files in os.walk(self.root_directory):
            for directory in directories:
                self._rename(broken=os.path.join(root, os.path.join(root, directory)) + os.sep,
                             fixed=os.path.join(root, self._fix_dir(directory)) + os.sep)
            for file in files:
                if file in self.exclude_files:
                    return
                self._rename(broken=os.path.join(root, file),
                             fixed=os.path.join(root, self._fix_file(file)))

    def _fix_file(
            self,
            name: str
    ) -> str:
        # fix filename characters
        name, extension = os.path.splitext(name)
        name = name.lstrip(' ').rstrip(' .')
        # fix filename length
        extension = extension.strip(' ')
        max_length = self.max_filename_length - len(extension)
        name = name[:max_length]
        # fix filename characters again
        name = name.lstrip(' ').rstrip(' .')
        # done
        return name + extension

    def _fix_dir(
            self,
            name: str
    ) -> str:
        return name.strip(' ')[:self.max_directory_length]

    def _rename(
            self,
            broken: str,
            fixed: str
    ) -> None:
        if broken == fixed:
            return
        if any(broken.startswith(entry) for entry in self.exclude_dirs):
            return
        print(f' BROKEN: "{broken}"\n    FIX: "{fixed}"')
        if os.path.exists(fixed):
            print('Cannot fix, target already exists.')
        elif input('Rename this? ') == 'y':
            os.rename(broken, fixed)
            print('Fixed.\n')
        else:
            print('Not fixed.\n')


def main() -> None:
    NameFix(
        root_directory='D:\\',
        exclude=['$RECYCLE.BIN'],
        max_directory_length=255,
        max_filename_length=143
    ).run()


if __name__ == '__main__':
    main()
