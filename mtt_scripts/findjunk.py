#!/usr/bin/python

import sys, chardet

RED = '\033[91m'
YELLOW = '\033[93m'
ENDC = '\033[0m'

numberOfParams = len(sys.argv)-1
if numberOfParams == 0:
  print('No string specified. Useage: mtt findjunk <string>')
  exit()

string = sys.argv[1]
encoding = chardet.detect(string.encode())['encoding']
print("ENCODING:" + encoding)
print(" ")
outputString=""
for char in string:
  charcode = ord(char)
  if charcode in [160, 8220, 8221, 8216, 8217]: #nbsp or “” or ‘’
    outputString += RED + '[' + str(charcode) + ']' + ENDC  
  elif charcode in [228, 229, 246]: #åäö
    outputString += char
  elif charcode < 32 or charcode > 126:
    outputString += YELLOW + '[' + str(charcode) + ']' + ENDC
  else:
    outputString += char

print(outputString)


