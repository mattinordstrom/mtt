#!/usr/bin/env python3
import os
import re
import shutil
import sys
from pathlib import Path

CLAUDE = Path(os.environ.get("CLAUDE_CONFIG_DIR") or Path.home() / ".claude")
CLAUDE_LABEL = str(CLAUDE).replace(str(Path.home()), "~", 1)
BOLD = "\033[1m"
DIM = "\033[2m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
END = "\033[0m"
if not sys.stdout.isatty():
    BOLD = DIM = CYAN = YELLOW = END = ""

WIDTH = shutil.get_terminal_size((120, 20)).columns
FULL = "-f" in sys.argv or "--full" in sys.argv


def frontmatter(path):
    try:
        text = path.read_text(errors="replace")
    except OSError:
        return {}
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    fields = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^\s*([\w-]+):\s*(.*)$", line)
        if kv:
            fields[kv.group(1)] = kv.group(2).strip().strip("\"'").replace('\\"', '"')
    return fields


def row(name, desc, name_width, tag="", indent=2):
    prefix = f"{' ' * indent}{CYAN}{name:<{name_width}}{END} "
    if tag:
        prefix += f"{YELLOW}{tag}{END} "
    visible = indent + name_width + 1 + (len(tag) + 1 if tag else 0)
    room = WIDTH - visible
    if not FULL and room > 10 and len(desc) > room:
        desc = desc[: room - 1] + "…"
    print(prefix + desc)


def header(title):
    print(f"\n{BOLD}{title}{END}")


def memories():
    header("MEMORIES")
    user_md = CLAUDE / "CLAUDE.md"
    if user_md.exists():
        print(f"  {CYAN}{CLAUDE_LABEL}/CLAUDE.md{END} {DIM}(global instructions, {len(user_md.read_text().splitlines())} lines){END}")
    home_prefix = re.sub(r"[^A-Za-z0-9]", "-", str(Path.home())) + "-"
    for mem_dir in sorted((CLAUDE / "projects").glob("*/memory")):
        files = sorted(f for f in mem_dir.glob("*.md") if f.name != "MEMORY.md")
        if not files:
            continue
        project = mem_dir.parent.name.removeprefix(home_prefix).removeprefix("projects-")
        print(f"  {BOLD}{project}{END} {DIM}({mem_dir}){END}")
        width = max(len(f.stem) for f in files)
        for f in files:
            fm = frontmatter(f)
            row(f.stem, fm.get("description", ""), width + 2, indent=4)


def skills():
    header(f"SKILLS  {CLAUDE_LABEL}/skills")
    entries = []
    for skill_md in sorted((CLAUDE / "skills").glob("*/SKILL.md")):
        fm = frontmatter(skill_md)
        manual = fm.get("disable-model-invocation") == "true"
        entries.append((fm.get("name") or skill_md.parent.name, fm.get("description", ""), manual))
    print_entries(entries)


def commands():
    header(f"COMMANDS  {CLAUDE_LABEL}/commands")
    entries = []
    for cmd in sorted((CLAUDE / "commands").rglob("*.md")):
        fm = frontmatter(cmd)
        name = "/" + str(cmd.relative_to(CLAUDE / "commands").with_suffix("")).replace(os.sep, ":")
        manual = fm.get("disable-model-invocation") == "true"
        entries.append((name, fm.get("description", ""), manual))
    print_entries(entries)


def print_entries(entries):
    if not entries:
        print(f"  {DIM}(none){END}")
        return
    width = max(len(e[0]) for e in entries) + 2
    any_manual = any(e[2] for e in entries)
    for name, desc, manual in entries:
        row(name, desc, width, ("[manual]" if manual else " " * 8) if any_manual else "")


if "-h" in sys.argv or "--help" in sys.argv:
    print("Usage: mtt claudeinv [-f|--full]\nList user-level Claude memories, skills and commands.\n"
          "Reads $CLAUDE_CONFIG_DIR if set, else ~/.claude.\n"
          "[manual] = disable-model-invocation: only you can run it, Claude never sees it.\n"
          "-f  don't truncate descriptions")
    sys.exit(0)

memories()
skills()
commands()
print(f"\n{DIM}[manual] = disable-model-invocation, not in Claude's context (hidden from /context){END}")
