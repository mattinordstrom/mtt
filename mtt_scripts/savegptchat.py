#!/usr/bin/python

import pyperclip
import json
import os
from datetime import datetime

BLUE = '\033[94m'
RED = '\033[91m'
ENDC = '\033[0m'

# Get JSON from clipboard
json_data = pyperclip.paste()

# Parse JSON
try:
    parsed_data = json.loads(json_data)
except json.JSONDecodeError:
    print(RED + "Sorry, there was an error decoding the JSON data." + ENDC)
    exit()

if 'mapping' not in parsed_data or len(parsed_data['mapping']) <= 0:
    print(RED + "mapping object is missing or empty in the JSON data. Did you copy the correct payload to clipboard?" + ENDC)
    exit()

# Output file
fileNameFromChatTitle = parsed_data['title']
fileNameFromChatTitle = ''.join(e for e in fileNameFromChatTitle if e.isalnum())
fileNameFromChatTitle = fileNameFromChatTitle.replace("å", "a").replace("ä", "a").replace("ö", "o").replace("Å", "A").replace("Ä", "A").replace("Ö", "O")
fileNameFromChatTitle = fileNameFromChatTitle + '_' + datetime.now().strftime("%HH%MM%SS") + '.txt'

FILE_PATH = "~/Desktop/gpt_chats/"
FILE_NAME = fileNameFromChatTitle
output_dir_path = os.path.expanduser(FILE_PATH)
os.makedirs(output_dir_path, exist_ok=True)
output_file_path = os.path.join(output_dir_path, FILE_NAME)

# Extract 'mapping' data and write to output file
with open(output_file_path, 'w', encoding='utf-8') as file:
    for key, value in parsed_data['mapping'].items():
        # Check if 'message' field exists
        if 'message' in value:
            role = value['message']['author']['role']
            for part in value['message']['content']['parts']:
                text = part
                file.write(f"{role}: \n{text}\n\n")

with open(output_file_path, 'r', encoding='utf-8') as file:
    print(file.read())

print("\n\n" + BLUE + FILE_PATH + FILE_NAME + ENDC)