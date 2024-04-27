#!/usr/bin/python

import sys

BOLD = '\033[1m'
YELLOW = '\033[93m'
ENDC = '\033[0m'

showMenu = len(sys.argv) < 2

print(' ')

if showMenu:
  print(BOLD+'Show all: mtt howto --showall'+ENDC)
  print(' ')
  print(YELLOW+'Use one of the following args:'+ENDC)
  print(' ')
  print('  find')
  print(' ')
  print('  git')
  print(' ')
  print('  grep')
  print(' ')
  print('  net')
  print(' ')
  print('  output')
  print(' ')
  print('  regex')
  print(' ')
  print('  sed')
  print(' ')
  print('  sort')
  print(' ')
  print('  xargs')
  print(' ')
  exit()

showAll = (sys.argv[1] == '--showall')


if showAll or sys.argv[1] == 'find':
  print(YELLOW+'________FIND________'+ENDC)
  print(' ')
  print(" Find all occurances of \"ENDC\" in files in mtt folder:")
  print( BOLD+" grep -i -Hr \"ENDC\" ~/projects_priv/mtt "+ENDC)
  print(' ')
  print(' ')
  print(" Find all occurances of \"FullScreen\" in xml files (including hidden) in projects folder:")
  print( BOLD+" sudo grep -Hr --include \*.xml \"FullScreen\" ~/projects "+ENDC)
  print(' ')
  print('------------------------')
  print(' ')
  print(" Find files starting with \"convert\":")
  print( BOLD+" find ~/projects_priv -type f -iname \"convert*\"  "+ENDC)
  print(' ')
  print(" Find in current folder:")
  print( BOLD+' find -type f -iname "convert*" '+ENDC)
  print(' ')
  print(" Case sensitive:")
  print( BOLD+' find -type f -name "convert*" '+ENDC)
  print(' ')
  print(" Include folders in search:")
  print( BOLD+' find ~/projects_priv -iname "convert*" '+ENDC)
  print(' ')

if showAll or sys.argv[1] == 'git':
  print(YELLOW+'________GIT________'+ENDC)
  print(' ')
  print(" Show stash list:")
  print( BOLD+" git stash list | head "+ENDC)
  print(' ')
  print(" Show changed files in a stash:")
  print( BOLD+" git stash show 2 | cat "+ENDC)
  print(' ')
  print('------------------------')
  print(' ')
  print(" List all branches that would be pruned:")
  print( BOLD+" git remote prune origin --dry-run"+ENDC)
  print(' ')
  print(" Prune the branches (delete ref to dead remote br):")
  print( BOLD+" git remote prune origin"+ENDC)
  print(' ')
  print(" Grep all merged branches (except develop and release branches):")
  print( BOLD+" git br --merged develop | grep -E 'conflict/|bugfix/|feature/'"+ENDC)
  print(' ')
  print(" Remove the local branches:")
  print( BOLD+" git br --merged develop | grep -E 'conflict/|bugfix/|feature/' | xargs -I {} git br -d {}"+ENDC)
  print(' ')
  print('------------------------')
  print(' ')
  print(" Show log of current branch commits:")
  print( BOLD+" git log --pretty=oneline --since=\"3 years ago\" | grep PROJECT-1234"+ENDC)
  print(' ')
  print(" Changes from other branch without commiting:")
  print( BOLD+" git log --pretty=format:'%H' --no-merges --reverse $(git merge-base master feature/SER-1234)..feature/SER-1234 | tr '\\n' ' '"+ENDC)
  print( BOLD+" git cherry-pick --no-commit <commit1> <commit2> <...>"+ENDC)
  print(' ')

if showAll or sys.argv[1] == 'grep':
  print(YELLOW+'________GREP________'+ENDC)
  print(' ')
  print(" List all ids that exists in both csv:")
  print( BOLD+" fgrep -wx -f listOfIds1.csv listOfIds2.csv >idsThatExistsInBothLists.csv "+ENDC)
  print(' ')
  print(" Remove ids from idsThatExistsInBothLists that are present in listOfIds3:")
  print( BOLD+" fgrep -wx -v -f listOfIds3.csv idsThatExistsInBothLists.csv >finalresult.csv "+ENDC)
  print(' ')

if showAll or sys.argv[1] == 'net':
  print(YELLOW+'________NET________'+ENDC)
  print(' ')
  print(" Print network device info:")
  print( BOLD+" ip addr | grep -A 999 -B 999 -E 'state UP|wlp|enx|10\.' "+ENDC)
  print(' ')
  print(" Scan network devices with nmap:")
  print( BOLD+" sudo nmap -sn 192.168.50.1/24"+ENDC)
  print(' ')

if showAll or sys.argv[1] == 'output':
  print(YELLOW+'________OUTPUT________'+ENDC)
  print(' ')
  print(" Print last lines of file out.txt every 3 seconds:")
  print( BOLD+" watch -n 3 tail out.txt "+ENDC)
  print(' ')
  print(" Print list with grep every 3 seconds:")
  print( BOLD+" watch -n 3 'ls -lAh | grep test123' "+ENDC)
  print(' ')
  print(" Print terminal output to file:")
  print( BOLD+' npm run dev 2>&1 | tee ~/Desktop/npm_run_output.txt'+ENDC)
  print(' ')

if showAll or sys.argv[1] == 'regex':
  print(YELLOW+'________REGEX________'+ENDC)
  print(' ')
  print(" Find all bananas and print 3 chars before and 9 chars after:")
  print( BOLD+" mtt fromc | grep -o -P '.{0,3}banana.{0,9}' "+ENDC)
  print(' ')
  print(" Find all Bananas print until comma sign:")
  print( BOLD+" grep -o -P '(Banana.*?),' < ./file1.csv > ~/Desktop/output.txt  "+ENDC)
  print(' ')
  print(" Find/replace captured group (intellij/vscode):")
  print( BOLD+' Search title attr in html: title="(.*)"(\/>*) '+ENDC)
  print( BOLD+' Replace with title tag: $2<title>$1</title> '+ENDC)
  print(' ')

if showAll or sys.argv[1] == 'sed':
  print(YELLOW+'________SED________'+ENDC)
  print(' ')
  print(" Replace apples with bananas in file:")
  print( BOLD+" sed -i 's/apple/banana/g' ~/Desktop/fruits.txt"+ENDC)
  print(' ')

if showAll or sys.argv[1] == 'sort':
  print(YELLOW+'________SORT________'+ENDC)
  print(' ')
  print(" Find duplicates:")
  print( BOLD+" mtt fromc | sort | uniq -cd"+ENDC)
  print(' ')

if showAll or sys.argv[1] == 'xargs':
  print(YELLOW+'________XARGS________'+ENDC)
  print(' ')
  print(" Create two text files:")
  print( BOLD+' printf "1\\n2\\n" | xargs -i touch {}.txt'+ENDC)
  print(' ')
  print(" Search each word in list and output occurences for each in file:")
  print( BOLD+' mtt fromc | xargs -I {} sh -c "grep -i {} file_with_many_rows.csv | wc -l"'+ENDC)
  print(' ')

