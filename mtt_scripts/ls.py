import os, stat, time, argparse, pwd
from tabulate import tabulate


BOLD_BLUE = '\033[1;94m'
GREEN = '\033[92m'
ENDC = '\033[0m'

def get_permissions(mode):
    """Get file permissions in numeric and symbolic form."""
    numeric = format(stat.S_IMODE(mode), '04o')
    symbolic = '-'
    if stat.S_ISDIR(mode):
        symbolic = 'd'
    elif stat.S_ISLNK(mode):
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

def format_size(size_in_bytes):
    if size_in_bytes >= 1024 * 1024 * 1024:
        size = round(size_in_bytes / (1024 * 1024 * 1024), 2)
        return f"{size} GiB"
    elif size_in_bytes >= 1024 * 1024:
        size = round(size_in_bytes / (1024 * 1024), 2)
        return f"{size} MiB"
    elif size_in_bytes >= 1024:
        size = round(size_in_bytes / 1024, 2)
        return f"{size} KiB"
    return f"{size_in_bytes} bytes"

def get_list_files(dir_to_list, show_only_directories, recursive=False):
    """List files and directories."""
    output = []
    dir_to_list = os.path.abspath(dir_to_list) 

    if recursive:
        for folder, subs, files in os.walk(dir_to_list):
            print(BOLD_BLUE + f"\n{folder}" + ENDC)

            for dir_name in subs:
                print(BOLD_BLUE + f"  {os.path.join(folder, dir_name)}" + ENDC)

            if not show_only_directories:
                for file_name in files:
                    print(f"  {os.path.join(folder, file_name)}")

        return []

    if not os.path.isdir(dir_to_list):
        # Mirror `ls <file>`: list the single entry instead of crashing.
        parent = os.path.dirname(dir_to_list.rstrip('/')) or '.'
        entries = [os.path.basename(dir_to_list.rstrip('/'))]
        dir_to_list = parent
    else:
        entries = os.listdir(dir_to_list)
    for entry in sorted(entries):
        full_path = os.path.join(dir_to_list, entry)
        try:
            st = os.lstat(full_path)
            mode = st.st_mode
            size_in_bytes = st.st_size
            mtime = time.strftime("%b %d %Y %H:%M", time.localtime(st.st_mtime))
            numeric_perm, symbolic_perm = get_permissions(mode)

            try:
                user = pwd.getpwuid(st.st_uid).pw_name
            except KeyError:
                user = str(st.st_uid)
            if len(user) > 10:
                user = user[:10] + "..."

            formattedName = entry
            if stat.S_ISDIR(mode):
                formattedName = BOLD_BLUE + entry + ENDC
            elif stat.S_ISLNK(mode):
                target = os.readlink(full_path)
                formattedName = formattedName + ' -> ' + target
            elif mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH):
                formattedName = GREEN + entry + ENDC

            size_str = format_size(size_in_bytes)

            if not show_only_directories or (show_only_directories and stat.S_ISDIR(mode)):
                output.append([symbolic_perm, numeric_perm, user, size_str, mtime, formattedName])
        except OSError as e:
            print(f"{type(e).__name__}: {full_path}: {e.strerror}")
    
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List files and directories.")
    parser.add_argument('-d', action='store_true', help='List only directories.')
    parser.add_argument('-r', action='store_true', help='Recursive.')
    parser.add_argument("dir_to_list", nargs="?", default=".", type=str, help="Directory to list (default: current directory).")
    args = parser.parse_args()

    dir_to_list = os.path.expanduser(args.dir_to_list.rstrip('/') + '/')
    
    output = get_list_files(dir_to_list, args.d, args.r)
    print(tabulate(output, headers=[], tablefmt="plain"))