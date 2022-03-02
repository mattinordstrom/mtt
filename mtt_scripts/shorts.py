#!/usr/bin/python

# Add this to .zshrc: 
# alias shorts="mtt shorts"

import sys

BOLD = '\033[1m'
YELLOW = '\033[93m'
ENDC = '\033[0m'

showAll = sys.argv[1] == ""

print(' ')

if showAll or sys.argv[1] == 'intellij':
  print(YELLOW+'::IntelliJ::'+ENDC)
  print(' Toggle bookmark on row:   ' + BOLD+'F11'+ENDC)
  print(' Show bookmarks:           ' + BOLD+'Shift + F11'+ENDC)
  print(' Next bookmark:            ' + BOLD+'Ctrl + Shift + Ä'+ENDC)
  print(' Previous bookmark:        ' + BOLD+'Ctrl + Shift + Ö'+ENDC)
  print(' Find action...:           ' + BOLD+'Ctrl + Shift + A'+ENDC)
  print(' ')

if showAll or sys.argv[1] == 'vscode':
  print(YELLOW+'::Visual Studio Code::'+ENDC)
  print(' Go to file:               ' + BOLD+'Ctrl + P'+ENDC)
  print(' Run command:              ' + BOLD+'Ctrl + Shift + P'+ENDC)
  print(' ')

if showAll or sys.argv[1] == 'dbeaver':
  print(YELLOW+'::DBeaver::'+ENDC)
  print(' New console:              ' + BOLD+'Ctrl + Alt + Enter'+ENDC)
  print(' Run template:             ' + BOLD+'Ctrl + Alt + Space'+ENDC)
  print(' Select data source:       ' + BOLD+'Ctrl + 9'+ENDC)
  print(' Select schema:            ' + BOLD+'Ctrl + 0'+ENDC)
  print(' ')

if showAll or sys.argv[1] == 'nano':
  print(YELLOW+'::Nano::'+ENDC)
  print(' Cut:                      ' + BOLD+'Ctrl + K'+ENDC)
  print(' Paste:                    ' + BOLD+'Ctrl + U'+ENDC)
  print(' Go to line:               ' + BOLD+'Alt + G'+ENDC)
  print(' Search forward:           ' + BOLD+'Ctrl + W (then Enter)'+ENDC)
  print(' Search backwards:         ' + BOLD+'Ctrl + Q (then Enter)'+ENDC)
  print(' Undo:                     ' + BOLD+'Alt + U'+ENDC)
  print(' Redo:                     ' + BOLD+'Alt + E'+ENDC)
  print(' Show line numbers:        ' + BOLD+'Alt + Shift + 3'+ENDC)
  print(' ')

print(' ')
