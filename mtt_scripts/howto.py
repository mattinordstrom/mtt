#!/usr/bin/python

import sys

BOLD = '\033[1m'
YELLOW = '\033[93m'
ENDC = '\033[0m'


def header(title):
    print(f"{YELLOW}________{title}________{ENDC}")
    print()


def example(desc, *cmds):
    print(f" {desc}:")
    for cmd in cmds:
        print(f"{BOLD} {cmd}{ENDC}")
    print()


def divider():
    print('------------------------')
    print()


def show_search():
    header('FIND')
    example('Find all occurances of "ENDC" in files in mtt folder',
            'grep -i -Hr "ENDC" ~/projects_priv/mtt')
    example('Find all occurances of "FullScreen" in xml files (including hidden) in projects folder',
            'sudo grep -Hr --include \\*.xml "FullScreen" ~/projects')
    divider()
    example('Find files starting with "convert"',
            'find ~/projects_priv -type f -iname "convert*"')
    example('Find in current folder (case sensitive)',
            'find -type f -name "convert*"')
    example('Include folders in search',
            'find ~/projects_priv -iname "convert*"')

    header('GREP')
    example('List all ids that exists in both csv',
            'fgrep -wx -f listOfIds1.csv listOfIds2.csv >idsThatExistsInBothLists.csv')
    example('Remove ids from idsThatExistsInBothLists that are present in listOfIds3',
            'fgrep -wx -v -f listOfIds3.csv idsThatExistsInBothLists.csv >finalresult.csv')

    header('SED')
    example('Replace apples with bananas in file',
            "sed -i 's/apple/banana/g' ~/Desktop/fruits.txt")

    header('SORT')
    example('Find duplicates',
            'mtt fromc | sort | uniq -cd')


def show_git():
    header('GIT')
    example('Merge master into feature branch',
            'git checkout feature/PROJ-1234',
            'git pull origin master',
            '(Fix merge conflict...)',
            'git commit',
            'git push origin HEAD')
    example('Show stash list',
            'git stash list | head')
    example('Show changed files in a stash',
            'git stash show stash@{2} | cat')
    divider()
    example('List all branches that would be pruned',
            'git remote prune origin --dry-run')
    example('Prune the branches (delete ref to dead remote br)',
            'git remote prune origin')
    example('Grep all merged branches (except develop and release branches)',
            "git br --merged develop | grep -E 'conflict/|bugfix/|feature/'")
    example('Remove the local branches',
            "git br --merged develop | grep -E 'conflict/|bugfix/|feature/' | xargs -I {} git br -d {}")
    divider()
    example('Show log of current branch commits',
            'git log --pretty=oneline --since="3 years ago" | grep PROJ-1234')
    example('Changes from other branch without commiting',
            "git log --pretty=format:'%H' --no-merges --reverse $(git merge-base master feature/PROJ-1234)..feature/PROJ-1234 | tr '\\n' ' '",
            'git cherry-pick --no-commit <commit1> <commit2> <...>')


def show_net():
    header('NET')
    example('Print network device info',
            "ip addr | grep -A 999 -B 999 -E 'state UP|wlp|enx|10\\.'")
    example('Scan network devices with nmap',
            'sudo nmap -sn 192.168.50.1/24')


def show_shell():
    header('OUTPUT')
    example('Print last lines of file out.txt every 3 seconds',
            'watch -n 3 tail out.txt')
    example('Print list with grep every 3 seconds',
            "watch -n 3 'ls -lAh | grep test123'")
    example('Print terminal output to file',
            'npm run dev 2>&1 | tee ~/Desktop/npm_run_output.txt')

    header('STAT')
    example('List rights of files in current dir',
            'stat -c "%A %a %n" *')

    header('XARGS')
    example('Create two text files',
            'printf "1\\n2\\n" | xargs -I {} touch {}.txt')
    example('Search each word in list and output occurences for each in file',
            'mtt fromc | xargs -I {} sh -c "grep -i {} file_with_many_rows.csv | wc -l"')


categories = {
    'search': show_search,
    'git': show_git,
    'net': show_net,
    'shell': show_shell,
}


print()

if len(sys.argv) < 2:
    print(BOLD + 'Show all: mtt howto --showall' + ENDC)
    print()
    print(YELLOW + 'Use one of the following args:' + ENDC)
    print()
    for name in categories:
        print('  ' + name)
    print()
    sys.exit()

arg = sys.argv[1]

if arg == '--showall':
    for fn in categories.values():
        fn()
elif arg in categories:
    categories[arg]()
