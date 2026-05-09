# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

`mtt` ("Mattis Terminal Toolkit") is a personal collection of small terminal helpers exposed under a single dispatcher command. It targets Linux (X11/xclip, apt/snap, `ss`, `fastfetch`, `exiftool`, `7z`, `wlp*`/`enp*` interface naming) and is not intended to be portable.

## Dispatcher and command resolution

`./mtt` (a bash script at the repo root) is the single entry point. `mtt <name> [args...]` resolves `<name>` against `mtt_scripts/` in this order — **first match wins**:

1. `mtt_scripts/<name>` — executable file (bash or otherwise), run directly with the remaining args.
2. `mtt_scripts/<name>.py` — Python file, run with `./.mtt_venv/bin/python3` (the project's venv, not system Python).
3. `mtt_scripts/<name>/main.go` — Go subcommand directory, run via `go run -C mtt_scripts/ ./<name> <args...>`.

`mtt h` / `mtt help` (and `-h`, `--help`, etc.) bypass the lookup and run `mtt_help.py` instead. Anything unmatched prints "Invalid. Use mtt h to see available commands".

Practical implication: when adding a new command, the filename in `mtt_scripts/` IS the subcommand name. There is no manifest. The shape (bare file vs. `.py` vs. `<dir>/main.go`) determines how it's invoked.

## Help registry is hand-maintained

`mtt_help.py` contains a hardcoded `scripts` list of `scriptInfo(name, category, description, params)` entries grouped by `scriptCategories` (`STRINGS`, `SYSTEM`, `DEV_TOOLS`, `MISC`). **Adding a new script in `mtt_scripts/` does not register it here automatically** — appending an entry to this list is a required second step, otherwise the command works but is invisible to `mtt h`.

## Languages and runtimes

- **Bash** for the dispatcher and most scripts. Many scripts use ANSI escape codes or `tput setaf` for color; expect them to be run in an interactive terminal.
- **Python 3.14** (pinned via `.python-version`) in a project-local venv at `.mtt_venv/`. All Python scripts run through this venv via the dispatcher; running them with system `python3` will likely fail on imports. Dependencies live in `requirements.txt` (`pyperclip`, `xmltodict`, `dicttoxml`, `defusedxml`, `chardet`, `tabulate`).
- **Go 1.25** module rooted at `mtt_scripts/` (single `go.mod`/`go.sum` shared by all Go subcommands). New Go commands go in `mtt_scripts/<name>/main.go` so the dispatcher's `go run -C mtt_scripts/ ./<name>` invocation finds them. Currently used for `uuidgen` (UUID/ULID + clipboard write via `golang.design/x/clipboard`).

## Setup

```sh
pyenv local 3.14
python3 -m venv .mtt_venv
./.mtt_venv/bin/python3 -m pip install -r requirements.txt
```

Add the repo to `PATH` (e.g. `export PATH=$PATH:$HOME/mtt` in `.zshrc`) so `mtt` is callable from anywhere.

Go dependencies are fetched on first `go run` (no separate install step).

## Clipboard conventions

Most "string" commands round-trip through the X11 clipboard:

- Bash scripts use `xclip -selection clipboard` (`toc`, `fromc`).
- Python scripts use `pyperclip` with `pyperclip.set_clipboard('xclip')` explicitly set — don't remove that line; the default backend selection is unreliable here.
- The Go `uuidgen` uses `golang.design/x/clipboard` and includes a 300ms `time.Sleep` after `clipboard.Write` because the clipboard daemon needs a moment to latch (see the TODO about switching to `wl-copy` on Wayland).

## Resources directory

`resources/` holds runtime state for `mtt compose`:

- `docker-compose_template.yaml` is checked in; `docker-compose.yaml` is gitignored and created by copying the template on first run of `mtt compose`.
- `resources/miniodata/`, `resources/minioconfig/`, `resources/mongodb_data/`, `resources/unifi-network-application/` are gitignored container volumes.

## External dependencies expected on PATH

These are not installed by the repo and several scripts will fail without them: `xclip`, `exiftool`, `fastfetch`, `ss` (iproute2), `7z`, `unzip`, `apt`, `snap`, `docker` (with compose plugin), and a Nerd Font terminal for `kittysetup`.
