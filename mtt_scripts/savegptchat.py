#!/usr/bin/python

import pyperclip
import json
import os

BLUE = '\033[94m'
RED = '\033[91m'
ENDC = '\033[0m'

# TODO error handling when content is not json

# TODO error when content is not correct json response from GET chat.openai.com/backend-api/conversation/<ID>

# Get JSON from clipboard
json_data = pyperclip.paste()

# Parse JSON
parsed_data = json.loads(json_data)

# Output file
FILE_PATH = "~/Desktop/gpt_chats/"
FILE_NAME = "gpt_chat_hist.txt" #TODO filename from title (and date)
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