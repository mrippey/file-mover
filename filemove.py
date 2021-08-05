import click 
import pathlib 
import shutil
import sys 
from rich import print 


def get_user_input(dirpath, extension, folder):
    user_defined_folder = pathlib.Path(folder)
    if not user_defined_folder.exists():
        user_defined_folder.mkdir()
    else:
        print('[bold red] Folder name exists, try another. [/]')
        sys.exit()

    user_dir_file_ext = pathlib.Path(dirpath).glob(extension)
    for specific_files in user_dir_file_ext:
        get_files_and_move(specific_files, user_defined_folder)


def get_files_and_move(specific_files, user_defined_folder) -> pathlib.Path:
    print(f'[bold green] {specific_files} was moved to {user_defined_folder}[/]\n')
    shutil.move(specific_files, user_defined_folder)
    

@click.command()
@click.argument('dirpath', type=click.Path())
@click.argument('extension', type=str)
@click.argument('folder', type=str)
def main(dirpath, extension, folder):
    """
    Small tool that accepts a directory path, file extension, and folder name. 
    The script will look for all file extensions identified by the user and move 
    said files to a folder specified by the user.

    ** Identify the extension by using '*.extension'

    Example:

    1. filemove.py /some/folder/path, '.py', 'Python Stuff'

    """

    return get_user_input(dirpath, extension, folder)

if __name__ == '__main__':
    main()