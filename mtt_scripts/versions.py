import subprocess
from typing import Sequence
from tabulate import tabulate

RED = '\033[91m'
GREEN = '\033[92m'
ENDC = '\033[0m'

ZWSP = "\u200B"

def get_version(cmd: Sequence[str]) -> str:
    result = RED +"NOT FOUND"+ENDC
    which = ""
    try:
        result = subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT)
        result = GREEN + result.splitlines()[0] + ENDC
        which = subprocess.check_output(["which", cmd[0]], text=True)
    except FileNotFoundError:
        result = RED +"NOT FOUND"+ENDC
    except Exception:
        result = RED +"ERROR"+ENDC

    return result, which

nodew = subprocess.check_output(["which", "node"], text=True)

phpv,phpw = get_version(["php", "-r", "echo rtrim(phpversion());"])
nodev,nodew = get_version(["node", "-v"])
npmv,npmw = get_version(["npm", "-v"])
javav,javaw = get_version(["java", "-version"])
mvnv,mvnw = get_version(["mvn", "--version"])
gov,gow = get_version(["go", "version"])
pythonv,pythonw = get_version(["python3", "-V"])
                           
output = [
    ["PHP", phpv, phpw],
    [ZWSP, ZWSP, ZWSP],
    ["NODE", nodev, nodew],
    ["NPM", npmv, npmw],
    [ZWSP, ZWSP, ZWSP],
    ["JAVA", javav, javaw],
    ["MAVEN", mvnv, mvnw],
    [ZWSP, ZWSP, ZWSP],
    ["GO", gov, gow],
    [ZWSP, ZWSP, ZWSP],
    ["PYTHON", pythonv, pythonw],
    [ZWSP, ZWSP, ZWSP],
]

print("\n")
print(tabulate(output, headers=[], tablefmt="simple"))
print("\n")