### Listbox with Add/Remove Functionality ###

import tkinter as tk
root = tk.Tk()
root.title("Listbox with Add/Remove Functionality")
root.geometry("600x450")

# Function to add item to Listbox 2
def add_item():
    selection = listbox1.curselection()
    if selection:
        item = listbox1.get(selection)
        listbox2.insert(tk.END, item)
        listbox1.delete(selection)

# Function to remove item from Listbox 2
def remove_item():
    selection = listbox2.curselection()
    if selection:
        item = listbox2.get(selection)
        listbox1.insert(tk.END, item)
        listbox2.delete(selection)

# Listbox 1  
listbox1 = tk.Listbox(root)
all_items = ["Apple", "Banana", "Mango", "Orange", "Watermelon", "Peach", "Plum"]
for item in all_items:
    listbox1.insert(tk.END, item)
listbox1.pack()

# Button to add item to Listbox 2
add_btn = tk.Button(root, text="Add Item to Listbox 2", command=add_item)
add_btn.pack()

# Listbox2
listbox2 = tk.Listbox(root)
all_items = ["Apple", "Tomato", "Pear", "Cherry", "Mango", "Coconut", "Avocado"]
for item in all_items:
    listbox2.insert(tk.END, item)
listbox2.pack()

# Button to remove item from Listbox 2
remove_btn = tk.Button(root, text="Remove Item from Listbox 2", command=remove_item)
remove_btn.pack()

root.mainloop()
    

