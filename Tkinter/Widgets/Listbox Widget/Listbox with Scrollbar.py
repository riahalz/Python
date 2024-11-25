### Listbox widget with scrollbar ###

import tkinter as tk
root = tk.Tk()
root.title("Listbox Widget with Scrollbar")
root.geometry("600x400")

# Scrollbar widget
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox3 = tk.Listbox(root, yscrollcommand = scrollbar.set)
for i in range(40):
    listbox3.insert(tk.END, f"Item[i+1]")
listbox3.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command = listbox3.yview)
