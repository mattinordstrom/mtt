import subprocess
from typing import Sequence
from tabulate import tabulate

RED = '\033[91m'
GREEN = '\033[92m'
ENDC = '\033[0m'


def get_version(cmd: Sequence[str]) -> str:
    result = RED +"NOT FOUND"+ENDC
    try:
        result = subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT)
        result = GREEN + result.splitlines()[0] + ENDC
    except FileNotFoundError:
        result = RED +"NOT FOUND"+ENDC
    except Exception:
        result = RED +"ERROR"+ENDC

    return result

output = [
    ["PHP", get_version(["php", "-r", "echo rtrim(phpversion());"])],
    ["", ""],
    ["NODE", get_version(["node", "-v"])],
    ["NPM", get_version(["npm", "-v"])],
    ["", ""],
    ["JAVA", get_version(["java", "-version"])],
    ["", ""],
    ["GO", get_version(["go", "version"])],
    ["", ""],
    ["PYTHON", get_version(["python3", "-V"])],
    ["", ""]
]

print("\n")
print(tabulate(output, headers=[], tablefmt="pipe"))
print("\n")