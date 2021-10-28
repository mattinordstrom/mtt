#!/usr/bin/python

import sys, subprocess

NUM_CHARS_BEFORE_DESCR = 47

GREEN = '\033[92m'
YELLOW = '\033[93m'
BOLD = '\033[1m'
ENDC = '\033[0m'

scriptCategories = {'STRINGS': 'String handling', 
                    'STATS': 'Stats', 
                    'DEV_TOOLS': 'Dev tools'}

class scriptInfo: 
    def __init__(self, name, category, description, params): 
        self.name = name
        self.category = category
        self.description = description
        self.params = params

numberOfParams = len(sys.argv)-1
if numberOfParams == 0:
    print('No arguments. Use mtt h to see available commands')
    exit()

scriptName = sys.argv[1]
paramsAsString = '"' + '" "'.join(sys.argv[2:]) + '"'
#print('Params as string: ' + paramsAsString)
#param1 = sys.argv[2]

scripts = [] 
scripts.append(scriptInfo('toc', 'STRINGS', 'To clipboard. Read file content or echo into clipboard.', ['?filepath']))
scripts.append(scriptInfo('fromc', 'STRINGS', 'From clipboard. Outputs clipboard content.', []))
scripts.append(scriptInfo('replacecc', 'STRINGS', 'Replaces given string with a new string in clipboard content.', ['find', 'new_string']))
scripts.append(scriptInfo('replaceccb', 'STRINGS', 'Replaces string between two strings in clipboard content. \nI.e <\"I have\"> <\"bananas\"> <\"99\">. I have 99 bananas', ['before', 'after', 'string']))
scripts.append(scriptInfo('base64', 'STRINGS', 'Encode/decode a base64 string.', ['string']))

scripts.append(scriptInfo('portuse', 'STATS', 'Display which process is using a specific port.', ['port']))
scripts.append(scriptInfo('topcpu', 'STATS', 'Displays top CPU usage.', []))
scripts.append(scriptInfo('topmem', 'STATS', 'Displays top MEM usage.', []))

scripts.append(scriptInfo('versions', 'DEV_TOOLS', 'Prints java, PHP, node, npm version info.', []))
scripts.append(scriptInfo('timestamp', 'DEV_TOOLS', 'Converts timestamp (ms) or date string (\"yyyy-mm-dd hh:mm:ss\"). \nIf no arg is passed the current timestamp (now) is printed.', ['?string']))
scripts.append(scriptInfo('localkafka', 'DEV_TOOLS', 'Starts local kafka server.', []))

if scriptName in ['h', 'help', '-h', '-help', '--h', '--help']:
  print('\n')
  print(BOLD + GREEN + '##### MTT - Mattis Terminal Toolkit #####\n' + ENDC)
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
else:
  validScript=False
  for obj in scripts:
    if scriptName == obj.name:
        validScript=True
  
  if validScript == True:
    subprocess.call([sys.path[0] + '/mtt_scripts/' + scriptName + ' ' + paramsAsString], shell=True)
  else:
    print('Invalid arguments. Use mtt h to see available commands')

print('\n')
