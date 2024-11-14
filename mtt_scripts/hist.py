#!/usr/bin/python3
import os, sys, pyperclip, datetime

GREEN = '\033[92m'
YELLOW = '\033[33m'
BLUE = '\033[94m'

BOLD_GREEN = '\033[1;92m'
BOLD_YELLOW = '\033[1;33m'
BOLD_BLUE = '\033[1;94m'

ITALIC = '\033[3m'
BOLD = '\033[1m'
ENDC = '\033[0m'


def read_last_lines(file_path, filter, num_lines=300):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
        
        # Get the last 5000 lines from zsh history
        last_lines = lines[-5000:]

        clean_lines = []
        for line in last_lines:
          clean_line = line.strip()
          timestamp = clean_line[clean_line.find(': ') + 2 : clean_line.find(':', 5)]
          clean_line = clean_line[clean_line.find(';') + 1:]

          if filter in line and not clean_line.startswith("history") and not clean_line.startswith("mtt hist"):
            clean_lines.append([clean_line, timestamp])

        # Return the last 300 lines of result
        return clean_lines[-num_lines:]

def main():
  print('\n')

  filter = ""
  if len(sys.argv) > 1:
    filter = sys.argv[1]

  home_path = os.path.expanduser("~")
  lines = read_last_lines(home_path+'/.zsh_history', filter)

  output_array = []
  for idx, line in enumerate(lines):
    output_array.append(line)

    dt_object = datetime.datetime.fromtimestamp(int(line[1]))
    readable_date = dt_object.strftime('%d/%m/%Y')

    if idx % 2 == 0:
      print(BOLD_BLUE + str(idx+1) + " -> " + ENDC + ITALIC + readable_date + ENDC + "  " + BLUE + line[0] + ENDC)
    else:
      print(BOLD_YELLOW + str(idx+1) + " -> " + ENDC + ITALIC + readable_date + ENDC + "  " + YELLOW + line[0] + ENDC)


  user_input = input("\nSelect a command to copy (enter 0 to exit): ")
  choice = int(user_input)

  if choice == 0:
    print("EXIT")
    sys.exit()
  elif choice > len(output_array):
    print("Invalid input!")
    sys.exit()

  pyperclip.set_clipboard('xclip')
  pyperclip.copy(output_array[choice-1][0])

  print(BOLD_GREEN+"\nCommand copied to clipboard!" + ENDC)



if __name__ == "__main__":
   main()