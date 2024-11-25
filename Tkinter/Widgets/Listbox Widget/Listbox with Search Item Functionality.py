### Listbox Widget with search item functionality ###

import tkinter as tk
root = tk.Tk()
root.title("Listbox Widget with Search Item Functionality")
root.geometry("600x400")

def search_listbox():
    search_item = entry.get().lower()
    listbox.delete(0, tk.END)
    for item in all_items:
        if search_item in item.lower():
            listbox.insert(tk.END, item)
            
entry = tk.Entry(root)
entry.pack()
search_btn = tk.Button(root, text="Search", command=search_listbox)
search_btn.pack()
        
listbox = tk.Listbox(root)
all_items = ["Apple", "Banana", "Mango", "Orange", "Melon", "Peach", "Plum", "Grape"]
for item in all_items:
    listbox.insert(tk.END, item)
listbox.pack()

root.mainloop()
