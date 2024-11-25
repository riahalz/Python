### Add Items to Combobox ###

import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Add Items to Combobox")
root.geometry("600x400")

items = ["Blue", "Red", "Yellow", "Purple", "Green"]

# Function to update label based on selection
def on_select(event):
    selected_item = combo.get()
    label_var.set(f"Selected: {selected_item}")

# Function to add new item to combobox and display it in label
def add_item():
    new_item = entry.get()
    if new_item and new_item not in items:
        items.append(new_item)
        combo['values'] = items  # Update combobox values
        label_var.set(f"New item added: {new_item}")
        entry.delete(0, tk.END)  # Clear entry field

# Combobox
combo = ttk.Combobox(root, values=items)
combo.bind("<<ComboboxSelected>>", on_select)
combo.pack(pady=10)

# Entry for adding new item
entry = tk.Entry(root)
entry.pack(pady=10)

# Button to add new item
add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.pack(pady=10)

# Label to display selected or added item
label_var = tk.StringVar()
label = tk.Label(root, textvariable=label_var)
label.pack(pady=10)

root.mainloop()
