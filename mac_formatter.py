import tkinter as tk
from tkinter import ttk

def to_columnt(s): 
    str_new = ''
    if '-' in s:
        str_new = s.replace('-', ':')
    else:  
        for i in range(0, len(s), 2):
            str_new += s[i:i+2] + ':'
        str_new = str_new[:-1]  
    return str_new

def to_minus(s):
    str_new = ''
    if ':' in s:
        str_new = s.replace(':', '-')
    else:  
        for i in range(0, len(s), 2):
            str_new += s[i:i+2] + '-'
        str_new = str_new[:-1]  
    return str_new

def to_noSpace(s):
    if ':' in s:
        str_new = s.replace(':', '')
    elif '-' in s:
        str_new = s.replace('-', '')
    return str_new

def perform_action(action):
    s = entry.get()
    if action == 'Add colon':
        result = to_columnt(s)
    elif action == 'Add minus':
        result = to_minus(s)
    elif action == 'Remove symbols':
        result = to_noSpace(s)
    result_label.config(text=f"Result: {result}")

def copy_to_clipboard(event):
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text").replace("Result: ", ""))
    root.update()  # Keeps the clipboard content after the window is closed

# Create the main window
root = tk.Tk()
root.title("MAC transformer")

# Create and place the widgets
entry_label = ttk.Label(root, text="Enter string:")
entry_label.grid(column=0, row=0, padx=10, pady=10)

entry = ttk.Entry(root, width=30)
entry.grid(column=1, row=0, padx=10, pady=10)

button_colon = ttk.Button(root, text="Add colon", command=lambda: perform_action('Add colon'))
button_colon.grid(column=0, row=1, padx=10, pady=10)

button_minus = ttk.Button(root, text="Add minus", command=lambda: perform_action('Add minus'))
button_minus.grid(column=1, row=1, padx=10, pady=10)

button_noSpace = ttk.Button(root, text="Remove colons", command=lambda: perform_action('Remove colons'))
button_noSpace.grid(column=2, row=1, padx=10, pady=10)

result_label = ttk.Label(root, text="Result:")
result_label.grid(column=0, row=2, columnspan=3, padx=10, pady=10)

# Bind double-click and right-click events to the result label
result_label.bind("<Double-1>", copy_to_clipboard)
result_label.bind("<Button-3>", copy_to_clipboard)

# Run the application
root.mainloop()
