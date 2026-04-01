import json
import os
import shutil
import subprocess
import sys
import urllib.request
import zipfile
import tempfile

HOME = os.path.expanduser("~")
CONFIG_DIR = os.path.join(HOME, ".config")
KITTY_CONFIG_DIR = os.path.join(CONFIG_DIR, "kitty")

FONT_DOWNLOAD_URL = "https://github.com/ryanoasis/nerd-fonts/releases/latest/download/FiraCode.zip"
FONTS_DIR = os.path.join(HOME, ".local", "share", "fonts")


def get_latest_github_version(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode())
    return data["tag_name"].lstrip("v")


def get_installed_kitty_version():
    try:
        out = subprocess.check_output(["kitty", "--version"], text=True, stderr=subprocess.DEVNULL)
        return out.split()[1]
    except (FileNotFoundError, IndexError):
        return None


def get_installed_starship_version():
    try:
        out = subprocess.check_output(["starship", "--version"], text=True, stderr=subprocess.DEVNULL)
        return out.splitlines()[0].split()[1]
    except (FileNotFoundError, IndexError):
        return None


def find_gists_dir():
    for candidate in [
        os.path.join(HOME, "projects", "gists"),
        os.path.join(HOME, "projects_priv", "gists"),
    ]:
        if os.path.isdir(candidate):
            return candidate
    return None


def copy_configs(gists_dir):
    starship_src = os.path.join(gists_dir, "starship.toml")
    kitty_conf_src = os.path.join(gists_dir, "kitty", "kitty.conf")

    if os.path.isfile(starship_src):
        os.makedirs(CONFIG_DIR, exist_ok=True)
        dest = os.path.join(CONFIG_DIR, "starship.toml")
        shutil.copy2(starship_src, dest)
        print(f"Copied starship.toml -> {dest}")
    else:
        print(f"WARNING: starship.toml not found at {starship_src}")

    if os.path.isfile(kitty_conf_src):
        os.makedirs(KITTY_CONFIG_DIR, exist_ok=True)
        dest = os.path.join(KITTY_CONFIG_DIR, "kitty.conf")
        shutil.copy2(kitty_conf_src, dest)
        print(f"Copied kitty.conf -> {dest}")
    else:
        print(f"WARNING: kitty.conf not found at {kitty_conf_src}")


def has_nerd_font():
    try:
        result = subprocess.check_output(["fc-list"], text=True, stderr=subprocess.DEVNULL)
        return "nerd" in result.lower()
    except FileNotFoundError:
        print("WARNING: fc-list not found, cannot check installed fonts")
        return False


def install_nerd_font():
    print("Nerd Font not found. Downloading FiraCode Nerd Font...")
    os.makedirs(FONTS_DIR, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmpdir:
        zip_path = os.path.join(tmpdir, "FiraCode.zip")

        print(f"Downloading from {FONT_DOWNLOAD_URL}")
        try:
            urllib.request.urlretrieve(FONT_DOWNLOAD_URL, zip_path)
        except Exception as e:
            print(f"ERROR: Download failed: {e}")
            sys.exit(1)

        print("Extracting fonts...")
        with zipfile.ZipFile(zip_path, "r") as zf:
            ttf_files = [f for f in zf.namelist() if f.endswith(".ttf")]
            for ttf in ttf_files:
                zf.extract(ttf, tmpdir)
                src = os.path.join(tmpdir, ttf)
                dest = os.path.join(FONTS_DIR, os.path.basename(ttf))
                shutil.copy2(src, dest)
                print(f"  Installed {os.path.basename(ttf)}")

    print("Refreshing font cache...")
    subprocess.run(["fc-cache", "-fv"], check=True)
    print("Nerd Font installed successfully.")


def list_kitty_fonts():
    print("\nFonts available in kitty:")
    try:
        subprocess.run(["kitty", "+list-fonts"], check=True)
    except FileNotFoundError:
        print("WARNING: kitty not found, cannot list fonts")


def install_kitty():
    current = get_installed_kitty_version()
    latest = get_latest_github_version("kovidgoyal", "kitty")

    if current and current == latest:
        print(f"Kitty already latest version {current}")
        return

    print("Installing kitty...")
    subprocess.run(
        "curl -L https://sw.kovidgoyal.net/kitty/installer.sh | sh /dev/stdin",
        shell=True,
        check=True,
    )

    if current:
        print(f"Updated kitty from version {current} to {latest}")
    else:
        print("kitty installed successfully.")


def install_starship():
    current = get_installed_starship_version()
    latest = get_latest_github_version("starship", "starship")

    if current and current == latest:
        print(f"Starship already latest version {current}")
        return

    print("Installing Starship...")
    subprocess.run(
        "curl -sS https://starship.rs/install.sh | sh -s -- -y",
        shell=True,
        check=True,
    )

    if current:
        print(f"Updated starship from version {current} to {latest}")
    else:
        print("Starship installed successfully.")


def main():
    install_kitty()
    install_starship()
    print()

    gists_dir = find_gists_dir()
    if not gists_dir:
        print("\033[91mERROR: No gists directory found\033[0m")
        sys.exit(1)
    print(f"Found gists directory: {gists_dir}")
    copy_configs(gists_dir)

    print()
    if has_nerd_font():
        print("Nerd Font already installed, skipping download.")
    else:
        install_nerd_font()

    #list_kitty_fonts()


main()
