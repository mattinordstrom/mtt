#!/usr/bin/python


import pyperclip

YELLOW = '\033[93m'
ENDC = '\033[0m'

pyperclip.set_clipboard('xclip')

inputString = pyperclip.paste()

outputString = inputString.replace('\r\n', '').replace('\n', '').replace('\r', '')

pyperclip.copy(outputString)

print("\n")
print(outputString)
print(YELLOW+"\n\nOutput has been copied to the clipboard!\n"+ENDC)



