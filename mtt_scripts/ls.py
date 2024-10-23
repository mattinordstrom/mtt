import os
import stat
import time
import argparse
import getpass

# TODO nicer output for file more than 1 mb
# TODO output as table

BLUE = '\033[94m'
ENDC = '\033[0m'

def print_row(mode, name, size, mtime, numeric_perm, symbolic_perm):
    formattedName = name
    if stat.S_ISDIR(mode):
        formattedName = BLUE + name + ENDC

    print(f"{symbolic_perm} {numeric_perm}  {size} kb  {mtime}  {formattedName}")

def get_permissions(mode):
    """Get file permissions in numeric and symbolic form."""
    numeric = oct(mode)[-3:]
    symbolic = '-'
    if stat.S_ISDIR(mode):
        symbolic = 'd'
    elif stat.S_ISLNK(mode): #TODO this is broken?
        symbolic = 'l'

    # User permissions
    symbolic += ''.join([
        'r' if mode & stat.S_IRUSR else '-',
        'w' if mode & stat.S_IWUSR else '-',
        'x' if mode & stat.S_IXUSR else '-'
    ])
    
    # Group permissions
    symbolic += ''.join([
        'r' if mode & stat.S_IRGRP else '-',
        'w' if mode & stat.S_IWGRP else '-',
        'x' if mode & stat.S_IXGRP else '-'
    ])
    
    # Other permissions
    symbolic += ''.join([
        'r' if mode & stat.S_IROTH else '-',
        'w' if mode & stat.S_IWOTH else '-',
        'x' if mode & stat.S_IXOTH else '-'
    ])
    
    return numeric, symbolic


def list_files(dir_to_list):
    """List files and directories."""
    dir_to_list = os.path.abspath(dir_to_list) 
    entries = os.listdir(dir_to_list)

    for entry in sorted(entries):
        full_path = os.path.join(dir_to_list, entry)
        try:
            mode = os.stat(full_path).st_mode
            size = f"{os.path.getsize(full_path) / 1024:.2f}"
            mtime = time.strftime("%b %d %Y %H:%M:%S", time.localtime(os.path.getmtime(full_path)))
            numeric_perm, symbolic_perm = get_permissions(mode)

            print_row(mode, entry, size, mtime, numeric_perm, symbolic_perm)
        except FileNotFoundError:
            print(f"FileNotFoundError: {full_path} not found")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List files and directories.")
    parser.add_argument("dir_to_list", nargs="?", default=".", help="Directory to list (default: current directory).")
    args = parser.parse_args()
    dir_to_list = str(args.dir_to_list)

    if(dir_to_list.startswith('~')):
        dir_to_list = dir_to_list.replace('~', '/home/' + getpass.getuser(), 1)

    list_files(dir_to_list.rstrip('/') + '/')
