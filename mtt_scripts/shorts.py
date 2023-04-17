#!/usr/bin/python

# Add this to .zshrc: 
# alias shorts="mtt shorts"

import sys

BOLD = '\033[1m'
YELLOW = '\033[93m'
ENDC = '\033[0m'

showAll = len(sys.argv) < 2

print(' ')

if showAll or sys.argv[1] == 'intellij':
  print(YELLOW+'________IntelliJ________'+ENDC)
  print(' Toggle bookmark on row:   ' + BOLD+'F11'+ENDC)
  print(' Show bookmarks:           ' + BOLD+'Shift + F11'+ENDC)
  print(' Next bookmark:            ' + BOLD+'Ctrl + Shift + Ä'+ENDC)
  print(' Previous bookmark:        ' + BOLD+'Ctrl + Shift + Ö'+ENDC)
  print(' Find action...:           ' + BOLD+'Ctrl + Shift + A'+ENDC)
  print(' ')
  print(' ')

if showAll or sys.argv[1] == 'vscode':
  print(YELLOW+'________Visual Studio Code________'+ENDC)
  print(' Go to file:               ' + BOLD+'Ctrl + P'+ENDC)
  print(' Run command:              ' + BOLD+'Ctrl + Shift + P'+ENDC)
  print(' Edit multiple rows:       ' + BOLD+'Shift + Alt + UpArrow/DownArrow'+ENDC)
  print(' ')
  print(' ')

if showAll or sys.argv[1] == 'dbeaver':
  print(YELLOW+'________DBeaver________'+ENDC)
  print(' New console:              ' + BOLD+'Ctrl + Alt + Enter'+ENDC)
  print(' Run template:             ' + BOLD+'Ctrl + Alt + Space'+ENDC)
  print(' Select data source:       ' + BOLD+'Ctrl + 9'+ENDC)
  print(' Select schema:            ' + BOLD+'Ctrl + 0'+ENDC)
  print(' ')
  print(' ')

if showAll or sys.argv[1] == 'nano':
  print(YELLOW+'________Nano________'+ENDC)
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

if showAll or sys.argv[1] == 'ubuntu':
  print(YELLOW+'________Ubuntu________'+ENDC)
  print(' Move win to other screen: ' + BOLD+'Super + Shift + LeftArrow/RightArrow'+ENDC)
  print(' Maximize/minimize win:    ' + BOLD+'Super + UpArrow/DownArrow'+ENDC)
  print(' ')
  print(' ')
  
if showAll or sys.argv[1] == 'terminator':
  print(YELLOW+'________Terminator________'+ENDC)
  print(' Switch tabs:  ' + BOLD+'Ctrl + PageUp/PageDown'+ENDC)
  print(' Focus win:    ' + BOLD+'Alt + Arrow key'+ENDC)
  print(' New win:      ' + BOLD+'Ctrl + Shift + I'+ENDC)
  print(' ')

print(' ')
