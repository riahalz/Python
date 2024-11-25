### Transfer Items to Listbox ###

import tkinter as tk
root = tk.Tk()
root.title("Transfer Items to Listbox")
root.geometry("600x400")

def data_transfer():
    selection = listbox1.curselection()
    if selection:
        item = listbox1.get(selection)
        listbox2.insert(tk.END, item)
        listbox1.delete(selection)
            
search_btn = tk.Button(root, text="Transfer Data to Listbox 2", command=data_transfer)
search_btn.pack()
        
listbox1 = tk.Listbox(root)
all_items = ["Apple", "Banana", "Mango", "Orange", "Melon", "Peach", "Plum", "Grape"]
for item in all_items:
    listbox1.insert(tk.END, item)
listbox1.pack()

listbox2 = tk.Listbox(root)
all_items = ["Apple", "Banana", "Mango", "Orange", "Melon", "Peach", "Plum", "Grape"]
for item in all_items:
    listbox2.insert(tk.END, item)
listbox2.pack()

root.mainloop()
    
