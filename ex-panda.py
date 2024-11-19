"""
Version beta 0.51
Developed by Email Zelman
"""

import keyboard
import os
import json
import tkinter as tk
from tkinter import ttk
from config_handler import trigger, match_suffix

abbrv_filename = os.path.join(os.getcwd(), 'abbreviations.json')        # Absolute path


def add_new_abbrv():
    new_abbrv = {add_abbrv_text.get():add_target_text.get()}
    json_data.update(new_abbrv)
    with open(abbrv_filename, 'w') as abbrv_json_file:
        json.dump(json_data, abbrv_json_file, indent = 2)
    update_labels()
    add_replacement_text(add_abbrv_text.get(), add_target_text.get())


label_frames = []   # List to keep track of created label frames
def update_labels():
    global label_frames
    for frame in label_frames:
        frame.destroy()
    label_frames = []

    for (abbrv, target) in json_data.items():
        abbrv_frame = ttk.Frame(master = window)
        abbrv_text = ttk.Label(master = abbrv_frame, text = abbrv)
        abbrv_target = ttk.Label(master = abbrv_frame, text = target)
        
        abbrv_text.pack(side = 'left')
        abbrv_target.pack(side = 'left', padx = 100)
        abbrv_frame.pack(pady = 5)
        label_frames.append(abbrv_frame)
        


def add_replacement_text(source_text, replacement_text):
    replacement = '\b'*(len(source_text)+1) + replacement_text
    callback = lambda: keyboard.write(replacement)
    keyboard.add_word_listener(source_text, callback, trigger, match_suffix, timeout=2)

# Check if the abbrv_list file exists in the current directory and create it if it doesn't
if not os.path.isfile(abbrv_filename):
    open(abbrv_filename, 'w').close()

# Load the json data and add the abbreviations using keyboard module

with open(abbrv_filename, 'r') as abbrv_json_file:
     json_data = json.load(abbrv_json_file)

for (abbrv, target) in json_data.items():
    add_replacement_text(abbrv, target)
    

# GUI setup
window = tk.Tk()
window.title('ex-panda v0.51')
window.geometry('500x600')
window.resizable(False, True)                           # TODO Check if height can be resized

# Adding new abbrv entries and variables
add_abbrv_text = tk.StringVar(value = '_abbrv')
add_target_text = tk.StringVar(value = 'target')
add_abbrv_frame = tk.Frame(master = window)
add_abbrv_entry = tk.Entry(master = add_abbrv_frame, textvariable = add_abbrv_text)
add_target_entry = tk.Entry(master = add_abbrv_frame, textvariable = add_target_text)

add_abbrv_frame.pack(side = 'top', pady = 10)
add_abbrv_entry.pack(side = 'left')
add_target_entry.pack(side = 'left')

# Adding new abbrv button
add_abbrv_button = tk.Button(master = window, text = 'Add new', command = lambda: add_new_abbrv())
add_abbrv_button.pack(side = 'top', pady = 5)

# Display labels upon launch (this func is also used to update the labels if new one is added)
update_labels()

# GUI main loop
window.mainloop()
