#!/usr/bin/python

import sys

NUM_CHARS_BEFORE_DESCR = 47

GREEN = '\033[92m'
YELLOW = '\033[93m'
BOLD = '\033[1m'
ENDC = '\033[0m'

scriptCategories = {'STRINGS': 'String handling',
                    'SYSTEM': 'System',
                    'DEV_TOOLS': 'Dev tools',
                    'MISC': 'Misc'}

class scriptInfo: 
    def __init__(self, name, category, description, params, isPython=False):
        self.name = name
        self.category = category
        self.description = description
        self.params = params
        self.isPython = isPython

scripts = [] 
scripts.append(scriptInfo('toc', 'STRINGS', 'To clipboard. Read file content or echo into clipboard.', ['?filepath']))
scripts.append(scriptInfo('fromc', 'STRINGS', 'From clipboard. Outputs clipboard content.', []))
scripts.append(scriptInfo('replacecc', 'STRINGS', 'Replaces given string with a new string in clipboard content.', ['find', 'new_string']))
scripts.append(scriptInfo('replaceccb', 'STRINGS', 'Replaces string between two strings in clipboard content. \nI.e <\"I have\"> <\"bananas\"> <\"99\">. I have 99 bananas', ['before', 'after', 'string']))
scripts.append(scriptInfo('base64', 'STRINGS', 'Encode/decode a base64 string.', ['string']))
scripts.append(scriptInfo('findjunk', 'STRINGS', 'Find junk signs in string.', ['string'], True))

scripts.append(scriptInfo('portuse', 'SYSTEM', 'Display which process is using a specific port.', ['port']))
scripts.append(scriptInfo('topcpu', 'SYSTEM', 'Displays top CPU usage.', []))
scripts.append(scriptInfo('topmem', 'SYSTEM', 'Displays top MEM usage.', []))
scripts.append(scriptInfo('fileinfo', 'SYSTEM', 'Get details about a file.', ['filepath']))
scripts.append(scriptInfo('appinfo', 'SYSTEM', 'App info. How and where it is installed.', ['appname']))

scripts.append(scriptInfo('versions', 'DEV_TOOLS', 'Prints java, PHP, node, npm version info.', []))
scripts.append(scriptInfo('timestamp', 'DEV_TOOLS', 'Converts timestamp (ms) or date string (\"yyyy-mm-dd hh:mm:ss\"). \nIf no arg is passed the current timestamp (now) is printed.', ['?string']))
scripts.append(scriptInfo('localkafka', 'DEV_TOOLS', 'Starts local kafka server.', []))
scripts.append(scriptInfo('convert', 'DEV_TOOLS', 'Converts xml/json from clipboard.', ['from_format', 'to_format'], True))
scripts.append(scriptInfo('uuid', 'DEV_TOOLS', 'Generate random uuid v4.', []))
scripts.append(scriptInfo('pyscratch', 'DEV_TOOLS', 'Creates python scratch file in ~/Desktop/py_scratches', [], True))
scripts.append(scriptInfo('goscratch', 'DEV_TOOLS', 'Creates golang scratch file in ~/Desktop/go_scratches', [], True))

scripts.append(scriptInfo('cat', 'MISC', 'List mtt scripts dir. Or outputs a scripts content.', ['?scriptname']))
scripts.append(scriptInfo('extract', 'MISC', 'Extract compressed file. (tar, 7z, zip...)', ['filepath']))
scripts.append(scriptInfo('shorts', 'MISC', 'List of keyboard shortcuts for different applications.', ['?application'], True))
scripts.append(scriptInfo('howto', 'MISC', 'Mixed howtos.', ['?application'], True))
scripts.append(scriptInfo('week', 'MISC', 'Output current week info. Date, day, week number etc.', []))
scripts.append(scriptInfo('calc', 'MISC', 'Calculator.', ['equation', '?numDecimals']))
scripts.append(scriptInfo('countdown', 'MISC', 'Countdown.', ['minutes']))
scripts.append(scriptInfo('savegptchat', 'MISC', 'Formatted GPT chat history from payload in clipboard', [], True))

print('\n')
print(BOLD + GREEN + '----- MTT - Mattis Terminal Toolkit -----\n' + ENDC)
print(BOLD + 'USAGE:\n' + ENDC)
#Loop through the categories
for key, value in scriptCategories.items():
  print(YELLOW + value + ENDC)
  #For each category loop through the scripts to find matching
  for script in scripts:
    if key == script.category:
      paramsString=''
      #Loop the parameters for current script
      for param in script.params:
        paramsString += '<' + param + '> '

      stringLength = 6 + len(script.name) + 1 + len(paramsString)
      numWhitespaces = NUM_CHARS_BEFORE_DESCR - stringLength
      whitespace = ' '
      description = script.description
      description = description.replace('\n', '\n'+((NUM_CHARS_BEFORE_DESCR+1)*whitespace))
      print('  mtt ' + script.name + ' ' + paramsString + (numWhitespaces*whitespace) + description)
  print('\n')
