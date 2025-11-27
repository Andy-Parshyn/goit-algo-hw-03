
from pathlib import Path
from shutil import copyfile
import sys


def read_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            read_folder(el)
        elif el.is_file(): 
            copy_file(el)


def copy_file(file: Path) -> None:
    ext = file.suffix
    new_path = output_folder / ext
    new_path.mkdir(exist_ok=True, parents=True)
    copyfile(file, new_path / file.name)



if __name__ == '__main__':
    try:
        if len(sys.argv) == 2:
            output = 'dist/'
        else:
            output = sys.argv[2]

        source = sys.argv[1]
        output_folder = Path(output)
        read_folder(Path(source))
    except IndexError:
        print('Invalid Path!')
    except IsADirectoryError as e:
        print(f'Something went wrong -> {e}')