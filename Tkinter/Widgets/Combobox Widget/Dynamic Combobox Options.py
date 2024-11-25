### Dynamic Combobox Options ###

import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Dynamic Combobox Options")
root.geometry("400x200")

# define function to add new option on button click
def add_option():
    options = combobox["values"]
    new_option = f"Option {len(options) + 1}"
    combobox["values"] = options + (new_option,)

# create Combobox widget
combobox = ttk.Combobox(root, values = ["Mango", "Orange", "Apple", "Banana"])
combobox.pack()

# create Button widget with command
button = ttk.Button(root, text = "Add New Option", command = add_option)
button.pack()

root.mainloop()
