#!/usr/bin/python

import sys

BOLD = '\033[1m'
YELLOW = '\033[93m'
ENDC = '\033[0m'

showAll = len(sys.argv) < 2

print(' ')

if showAll or sys.argv[1] == 'regex':
  print(YELLOW+'::REGEX::'+ENDC)
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

if showAll or sys.argv[1] == 'grep':
  print(YELLOW+'::GREP::'+ENDC)
  print(" List all ids that exists in both csv:")
  print( BOLD+" fgrep -wx -f listOfIds1.csv listOfIds2.csv >idsThatExistsInBothLists.csv "+ENDC)
  print(' ')
  print(" Remove ids from idsThatExistsInBothLists that are present in listOfIds3:")
  print( BOLD+" fgrep -wx -v -f listOfIds3.csv idsThatExistsInBothLists.csv >finalresult.csv "+ENDC)
  print(' ')

if showAll or sys.argv[1] == 'watch':
  print(YELLOW+'::WATCH::'+ENDC)
  print(" Print last lines of file out.txt every 3 seconds:")
  print( BOLD+" watch -n 3 tail out.txt "+ENDC)
  print(' ')

if showAll or sys.argv[1] == 'git':
  print(YELLOW+'::GIT::'+ENDC)
  print(" Show stash list:")
  print( BOLD+" git stash list | head "+ENDC)
  print(' ')
  print(" Show changed files in a stash:")
  print( BOLD+" git stash show 2 | cat "+ENDC)
  print(' ')

print(' ')
