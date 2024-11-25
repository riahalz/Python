### Combobox with Changing Label Text ###

import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Combobox with Changing Label Text")
root.geometry("400x200")

# Combobox with options
options = ["Option 1", "Option 2", "Option 3", "Option 4"]
combobox = ttk.Combobox(root, values = options)
combobox.pack()

# Function to change label text
def display_selected():
    selected_option = combobox.get()
    label.config(text=f"{selected_option}")

# Function to add item to list
def add_item():
    additem = entrybox.get()
    combobox.insert(tk.END, additem)

# Label to display selected option
label = tk.Label(root, text="No Option Selected", font=("Arial", 16))
label.pack(pady=20)

# Select button
select_btn = tk.Button(root, text="Select", command=display_selected)
select_btn.pack()

label2 = tk.Label(root, text="Add Item to Combobox", font=("Arial", 16))
label2.pack()

# Text entry widget
entrybox = tk.Entry(root, font=("Arial", 16))
entrybox.pack()

# Add item Button
select_btn = tk.Button(root, text="Add Item to Combobox", command=add_item)
select_btn.pack()

root.mainloop()
