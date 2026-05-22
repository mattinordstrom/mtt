#!/usr/bin/python


import sys

import pyperclip

YELLOW = '\033[93m'
ENDC = '\033[0m'

separator = ' ' if '-s' in sys.argv[1:] else ''

pyperclip.set_clipboard('xclip')

inputString = pyperclip.paste()

outputString = inputString.replace('\r\n', separator).replace('\n', separator).replace('\r', separator)

pyperclip.copy(outputString)

print("\n")
print(outputString)
print(YELLOW+"\n\nOutput has been copied to the clipboard!\n"+ENDC)



