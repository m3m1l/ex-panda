"""
Version beta 0.4
Developed by Email Zelman
"""

import keyboard
import os
import json
from config_handler import trigger, match_suffix

abbrv_filename = os.path.join(os.getcwd(), 'abbreviations.json')       # Absolute path


def add_replacement_text(source_text, replacement_text):
    replacement = '\b'*(len(source_text)+1) + replacement_text
    callback = lambda: keyboard.write(replacement)
    keyboard.add_word_listener(source_text, callback, trigger, match_suffix, timeout=2)

# Check if the abbrv_list file exists in the current directory and create it if it doesn't
if not os.path.isfile(abbrv_filename):
    open(abbrv_filename, 'w').close()

print('========================= Loading abbreviation file... ====================')

with open(abbrv_filename, 'r') as abbrv_json_file:
     json_data = json.load(abbrv_json_file)

for (abbrv, target) in json_data.items():
    print('\nabbrv :', abbrv, '\ntarget :\n', target)
    add_replacement_text(abbrv, target)

print('\n========================= Loading finished ====================')
print('Using the following trigger:', trigger)


keyboard.wait()