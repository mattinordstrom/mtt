#!/usr/bin/python3
import os, sys, pyperclip

def read_last_lines(file_path, filter, num_lines=1000):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
        
        last_lines = lines[-num_lines:]

        clean_lines = []
        for line in last_lines:
          clean_line = line.strip()
          clean_line = clean_line[clean_line.find(';') + 1:]
          if filter in line and not clean_line.startswith("history ") and not clean_line.startswith("mtt hist "):
            clean_lines.append(clean_line)

        return clean_lines


print('\n')
filter = sys.argv[1]

home_path = os.path.expanduser("~")
lines = read_last_lines(home_path+'/.zsh_history', filter, 1000)

output_array = []
for idx, line in enumerate(lines):
  output_array.append(line)
  print(idx+1, "-> "+line)


user_input = input("\nSelect a command to copy (enter 0 to exit): ")
choice = int(user_input)

if choice == 0:
  print("EXIT")
  sys.exit()
elif choice > len(output_array):
  print("Invalid input!")
  sys.exit()

pyperclip.set_clipboard('xclip')
pyperclip.copy(output_array[choice-1])

print("Command copied to clipboard!")