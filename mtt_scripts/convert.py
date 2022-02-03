#!/usr/bin/python

# pip install pyperclip dicttoxml xmltodict

import pyperclip, json, xmltodict, sys
from xml.dom.minidom import parseString
from dicttoxml import dicttoxml

YELLOW = '\033[93m'
ENDC = '\033[0m'

fromFormat = sys.argv[1]
toFormat = sys.argv[2]
input = pyperclip.paste()

print(YELLOW+"Input: "+ENDC, input[0:50]+"...")
print(" ")

if toFormat == 'xml':
  if fromFormat == 'json':
    input = json.loads(input)  
    xml_str = dicttoxml(input, attr_type = False)
    dom = parseString(xml_str)
    pyperclip.copy(dom.toprettyxml())
  elif fromFormat == 'xml':
    dom = parseString(input)
    pyperclip.copy(dom.toprettyxml())

  print(YELLOW+"Output"+ENDC+" XML has been copied to the clipboard!")
elif toFormat == 'json':
  if fromFormat == 'json':
    output = json.loads(input)
    pyperclip.copy(json.dumps(output, indent=2))
  elif fromFormat == 'xml':
    output = xmltodict.parse(input)
    pyperclip.copy(json.dumps(output, indent=2))

  print(YELLOW+"Output"+ENDC+" JSON has been copied to the clipboard!")
