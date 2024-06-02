"""
Version beta 0.314159
Developed by Email Zelman
"""

import keyboard
import re
import os
from config_handler import shrtct, match_suffix

abbrv_dict = {}
cwd = os.getcwd()
abbrv_filename = os.path.join(cwd, 'abbrv_list.txt')       # Absolute path

def add_replacement_text(source_text, replacement_text):
    replacement = '\b'*(len(source_text)+1) + replacement_text
    callback = lambda: keyboard.write(replacement)
    keyboard.add_word_listener(source_text, callback, shrtct, match_suffix, timeout=2)

# Check if the abbrv_list file exists in the current directory and create it if it doesn't
if not os.path.isfile(abbrv_filename):
    open(abbrv_filename, 'w').close()

print('========================= Loading abbreviation file... ====================')

with open(abbrv_filename, 'r') as abbr_file:
    for line in abbr_file:
        match = re.match(r"'([^']*)' '((?:[^'\\]|\\.)*)'", line.strip())
        if match:
            key = match.group(1)
            abbrv = match.group(2).replace("\\'", "'").replace("\\n", "\n")
            abbrv_dict[key] = abbrv

for (abbrv, target) in abbrv_dict.items():
    add_replacement_text(abbrv, target)
    print('\nabbrv :', abbrv, '\ntarget :\n', target)

print('\n========================= Loading finished ====================')
print('Using the following shortcut:', shrtct)

keyboard.wait()