### Listbox Widget ###

import tkinter as tk
root = tk.Tk()
root.title("Listbox Widget")
root.geometry("600x400")

## Listbox widget
listbox1 = tk.Listbox(root)
listbox1.insert(tk.END, "Python")
listbox1.insert(tk.END, "Java")
listbox1.insert(tk.END, "C++")
listbox1.insert(tk.END, "Ruby")

listbox1.pack()

## Listbox with multiple option selections
listbox2 = tk.Listbox(root, bg = "violet", selectmode = tk.MULTIPLE)
listbox2.insert(tk.END, "Mango")
listbox2.insert(tk.END, "Apple")
listbox2.insert(tk.END, "Banana")
listbox2.insert(tk.END, "Grape")
listbox2.insert(tk.END, "Orange")
listbox2.insert(tk.END, "Peach")
listbox2.insert(tk.END, "Plum")
listbox2.insert(tk.END, "Watermelon")

listbox2.pack()

root.mainloop()
