"""
Ex-panda 1.0, a lightweight text expander
Developed by Emil Zieliński
"""

import os
import json
import keyboard
import tkinter as tk
from webbrowser import open_new
from tkinter import ttk, PhotoImage

def edit_button_function(label_key):
    def confirm_edit():
        new_value = value_entry.get()
        target_labels[label_key].config(text=new_value)
        json_data[label_key] = new_value
        save_json_data(abbrv_filename, json_data)
        
        reload_config(json_data)
        edit_window.destroy()

    def cancel_edit():
        edit_window.destroy()

    # Create new window for editing
    edit_window = tk.Toplevel(window)
    edit_window.title("Edit Abbreviation")
    edit_window.geometry(center_window(300, 200))
    edit_window.resizable(False, False)
    edit_window.configure(bg='#c7c7cc')

    key_label = tk.Label(edit_window, text=f"Key: {truncate_text(label_key, 20)}", bg='#c7c7cc')
    key_label.pack(pady=20)

    value_label = tk.Label(edit_window, text="New value:", bg='#c7c7cc')
    value_label.pack()
    value_entry = ttk.Entry(edit_window)
    value_entry.insert(0, target_labels[label_key].cget("text"))
    value_entry.pack(pady=5)

    # Confirm button
    confirm_button_image = PhotoImage(file="images/confirm_button_image.png")
    images.append(confirm_button_image)
    confirm_button = tk.Button(
        edit_window,
        command = confirm_edit,
        image = confirm_button_image, 
        borderwidth=0)
    confirm_button.pack(side="left", padx=20, pady=10)

    # Cancel button
    cancel_button_image = PhotoImage(file="images/cancel_button_image.png")
    images.append(cancel_button_image)
    cancel_button = tk.Button(
        edit_window, 
        command = cancel_edit, 
        image = cancel_button_image, 
        borderwidth=0)
    cancel_button.pack(side="right", padx=20, pady=10)

def delete_button_function(label_key):
    def confirm_delete():
        # Destroy the frame associated with the label
        if label_key in frames:
            frames[label_key].destroy()

        # Remove from dictionaries
        if label_key in abbrv_labels:
            del abbrv_labels[label_key]
        if label_key in target_labels:
            del target_labels[label_key]
        if label_key in frames:
            del frames[label_key]

        remove_word_listener(label_key)

        # Remove from json_data and update the file
        json_data.pop(label_key)
        save_json_data(abbrv_filename, json_data)
        
        update_scrollregion()
        confirm_window.destroy()

    def cancel_delete():
        confirm_window.destroy()

    # Confirmation window
    confirm_window = tk.Toplevel(window)
    confirm_window.title("Confirm Deletion")
    confirm_window.geometry(center_window(250, 150))
    confirm_window.resizable(False, False)
    confirm_window.configure(bg='#c7c7cc')

    confirm_label = tk.Label(
        confirm_window, 
        text=f"Are you sure you want to delete {truncate_text(label_key, 15)}?", 
        wraplength=200, 
        bg='#c7c7cc')
    confirm_label.pack(pady=20)

    confirm_button_image = PhotoImage(file="images/confirm_button_image.png")
    images.append(confirm_button_image)
    confirm_button = tk.Button(
        confirm_window, 
        text="Yes", 
        command=confirm_delete, 
        image = confirm_button_image, 
        borderwidth=0)
    confirm_button.pack(side="left", padx=20, pady=10)

    cancel_button_image = PhotoImage(file="images/cancel_button_image.png")
    images.append(cancel_button_image)
    cancel_button = tk.Button(
        confirm_window, 
        text="No", 
        command=cancel_delete, 
        image = cancel_button_image, 
        borderwidth=0)
    cancel_button.pack(side="right", padx=20, pady=10)

def info_button_function():
    def callback(url):
        open_new(url)

    info_window = tk.Toplevel(window)
    info_window.title("About")
    info_window.resizable(False, False)
    info_window.configure(bg='#c7c7cc')
    info_window.geometry(center_window(250, 150))

    about_label = tk.Label(info_window, text="Code and layout:\n\n\nGraphic design:", bg='#c7c7cc', font=('Helvetica', 10, 'bold'))
    about_label.grid(row=0, column=0, padx=10, pady=10)

    names_label = tk.Label(info_window, text="Emil Zieliński\n\n\nMaciej Makoś", bg='#c7c7cc')
    names_label.grid(row=0, column=1, padx=20, pady=10)

    link_label = tk.Label(info_window, text="Project site", fg="blue", cursor="hand2", bg='#c7c7cc')
    link_label.grid(row=1, column=0, columnspan=2, pady=10)
    link_label.bind("<Button-1>", lambda e: callback("https://github.com/m3m1l/ex-panda"))

def refresh_button_function():
    for abbrv, target in json_data.items():
        frames[abbrv].destroy()
        del abbrv_labels[abbrv]
        del target_labels[abbrv]
        del frames[abbrv]
    reload_config(json_data)
    for abbrv, target in json_data.items():
        add_new_frame(abbrv, target)


def add_new_frame(abbrv, target):
    new_abbrv_frame = ttk.Frame(content_frame, width=400, height=40)
    new_abbrv_frame.pack_propagate(False)
    new_abbrv_frame.pack(side="top", pady=2)
    frames[abbrv] = new_abbrv_frame

    # Key label
    abbrv_label = ttk.Label(new_abbrv_frame, background='#c7c7cc', text=truncate_text(abbrv))
    abbrv_label.place(x=10, y=0, width=100, height=30)
    abbrv_labels[abbrv] = abbrv_label

    # Target label
    target_label = ttk.Label(new_abbrv_frame, background="#d3d3d3", text=truncate_text(target))
    target_label.place(x=120, y=0, width=190, height=30)
    target_labels[abbrv] = target_label

    # Edit button
    edit_button_image = PhotoImage(file="images/edit_button.png")
    images.append(edit_button_image)
    edit_button = tk.Button(
        new_abbrv_frame,
        text="edit",
        image=edit_button_image,
        borderwidth=0,
        command=lambda k=abbrv: edit_button_function(k),
    )
    edit_button.place(x=320, y=0, width=30, height=30)

    # Delete button
    delete_button_image = PhotoImage(file="images/delete_button.png")
    images.append(delete_button_image)
    delete_button = tk.Button(
        new_abbrv_frame,
        text="del",
        image=delete_button_image,
        borderwidth=0,
        command=lambda k=abbrv: delete_button_function(k),
    )
    delete_button.place(x=360, y=0, width=30, height=30)
    update_scrollregion()
    canvas.update_idletasks()

def contains_whitespace(text):
    for char in text:
        if char.isspace():
            return True
    return False

def add_button_function():
    def confirm_add_new():
        abbrv = abbrv_entry.get()
        if abbrv in json_data:
            already_exists_err()
        elif abbrv == '':
            abbrv_empty_err()
        elif contains_whitespace(abbrv):
            no_white_chars_err()
        else:
            target = target_entry.get()
            add_word_listener(abbrv, target)
            json_data[abbrv] = target
            save_json_data(abbrv_filename, json_data)

            # Create and display the new frame for the abbreviation
            add_new_frame(abbrv, target)
            update_scrollregion()
            add_window.destroy()

    def cancel_add_new():
        add_window.destroy()
    
    def already_exists_err():        
        if not hasattr(already_exists_err, "has_run"):
            already_exists_err.has_run = True
            error_label = tk.Label(master = add_window, text=f'Error: Already exists!')
            error_label.pack(pady = 5)

    def abbrv_empty_err():
        if not hasattr(abbrv_empty_err, "has_run"):
            abbrv_empty_err.has_run = True
            error_label = tk.Label(master = add_window, text=f'Error: Can\'t be empty!')
            error_label.pack(pady = 5)

    def no_white_chars_err():
        if not hasattr(no_white_chars_err, "has_run"):
            no_white_chars_err.has_run = True
            error_label = tk.Label(master = add_window, text=f'Spacebar disallowed!')
            error_label.pack(pady = 5)

    add_window = tk.Toplevel(window)
    add_window.title("Add New Abbreviation")
    add_window.geometry(center_window(300, 200))
    add_window.resizable(False, False)
    add_window.configure(bg='#c7c7cc')


    key_label = tk.Label(add_window, text="New abbreviation:", bg='#c7c7cc')
    key_label.pack(pady=10)
    
    abbrv_entry = ttk.Entry(add_window)
    abbrv_entry.pack()

    value_label = tk.Label(add_window, text="New target:", bg='#c7c7cc')
    value_label.pack()

    target_entry = ttk.Entry(add_window)
    target_entry.pack(pady=5)

    # Confirm button
    confirm_button_image = PhotoImage(file="images/confirm_button_image.png")
    images.append(confirm_button_image)
    confirm_button = tk.Button(
        add_window,
        command=confirm_add_new,
        image=confirm_button_image, 
        borderwidth=0)
    confirm_button.pack(side="left", padx=20, pady=10)

    # Cancel button
    cancel_button_image = PhotoImage(file="images/cancel_button_image.png")
    images.append(cancel_button_image)
    cancel_button = tk.Button(
        add_window,
        command=cancel_add_new, 
        image=cancel_button_image, 
        borderwidth=0)
    cancel_button.pack(side="right", padx=20, pady=10)
    
# Make the pop up windows appear in the middle of main window
def center_window(width, height):
    main_window_x = window.winfo_x()
    main_window_y = window.winfo_y()
    main_window_width = window.winfo_width()
    main_window_height = window.winfo_height()

    x = main_window_x + (main_window_width // 2) - (width // 2)   # 250 - window width
    y = main_window_y + (main_window_height // 2) - (height // 2)  # 150 - window height

    return f"{width}x{height}+{x}+{y}"
    
def update_scrollregion():
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

def truncate_text(text, max_length=60):
    if len(text) > max_length:
        return text[:max_length - 3] + "..."
    return text
    
# ======= EXPANDA PART ======

def add_word_listener(abbrv, target):
    keyboard.add_abbreviation(abbrv, target, match_suffix=True, timeout=5)

def remove_word_listener(abbrv):
    keyboard.remove_word_listener(abbrv)

def load_json_file(filename):
    if not os.path.isfile(filename):                            # Check if the abbreviation file exists and create it if necessary
        with open(filename, 'w') as abbrv_json_file:
            dummy_data = {'txt': 'your text here'}
            json.dump(dummy_data, abbrv_json_file, indent = 2)
        abbrv_json_file.close()
        
    try:
        with open(abbrv_filename, 'r') as abbrv_json_file:
            json_data = json.load(abbrv_json_file)
            abbrv_json_file.close()
            return json_data
    except Exception:
        print('The abbreviations.json file is corrupted.\nRemove the file and open the application again.')
        exit(-1)

def save_json_data(filename, json_data):
    with open(filename, 'w') as abbrv_json_file:
        json.dump(json_data, abbrv_json_file, indent = 2)

def add_abbreviation(abbrv, target):
    add_word_listener(abbrv, target)
    json_data.update({abbrv:target})
    save_json_data(abbrv_filename, json_data)

def del_abbreviation(abbrv):
    remove_word_listener(abbrv)
    json_data.pop(abbrv)
    save_json_data(abbrv_filename, json_data)

def ren_abbreviation(abbrv, new_target):
    json_data[abbrv] = new_target
    save_json_data(abbrv_filename, json_data)
    reload_config(json_data)

def reload_config(json_data):
    for (abbrv, target) in json_data.items():
        remove_word_listener(abbrv)
    json_data = {}
    json_data = load_json_file(abbrv_filename)
    for (abbrv, target) in json_data.items():
        add_word_listener(abbrv, target)

# Load all abbreviations from json on start. All loaded abbreviations will be stored in "json_data" var
abbrv_filename = os.path.join(os.getcwd(), 'abbreviations.json')            # Absolute path
json_data = load_json_file(abbrv_filename)
for (abbrv, target) in json_data.items():
        add_word_listener(abbrv, target)

# ======= GUI setup =======
window = tk.Tk()
window.title("ex-panda v1.0")
window.geometry("420x550")
window.resizable(False, False)
window.iconbitmap("images/expanda.ico")

# ======= Top Section with Buttons =======
top_section_frame = tk.Frame(window, width=400, height=80)
top_section_frame.pack_propagate(False)
top_section_frame.pack(side="top", fill="x")

# Refresh button
refresh_button_image = PhotoImage(file="images/refresh_button.png")
refresh_button = tk.Button(
    master=top_section_frame,
    text="refresh",
    image=refresh_button_image,
    borderwidth=0,
    command = lambda: refresh_button_function()
)
refresh_button.place(x=30, y=15, width=40, height=40)

# Add new button
add_button_image = PhotoImage(file="images/add_button.png")
add_button = tk.Button(
    master=top_section_frame, 
    image=add_button_image, 
    borderwidth=0,
    command = lambda: add_button_function())
add_button.place(x=130, y=10, width=140, height=50)

# Info button
info_button_image = PhotoImage(file="images/info_button.png")
info_button = tk.Button(
    master=top_section_frame, 
    image=info_button_image, 
    borderwidth=0, 
    command = lambda: info_button_function())
info_button.place(x=330, y=15, width=40, height=40)

# ======= Main Content Section with Scrollbar =======
container = ttk.Frame(window)
container.pack(fill="both", expand=True)

canvas = tk.Canvas(container, width=400, height=470)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

content_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# ======= Labels and frames =======
abbrv_labels = {}
target_labels = {}
frames = {}

# Button images must be stored to prevent garbage collection
images = []

# ======= Scroll Section with abbreviations =======
for abbrv, target in json_data.items():
    add_new_frame(abbrv, target)

# ======= Main Loop =======
window.mainloop()