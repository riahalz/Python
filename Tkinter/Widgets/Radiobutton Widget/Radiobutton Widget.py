### Radiobutton - Radio Button Widget ###

import tkinter as tk
from tkinter import scrolledtext
root = tk.Tk()
root.title("Radiobutton - Radio Button Widget")
root.geometry("400x200")

# create a Tkinter variable
var = tk.StringVar(value = "Python") # set default selected value to Python 

# create radio button widgets
radiobuttons = [("Python", "Python"),
                ("Java", "Java"),
                ("C++", "C++"),
                ("JavaScript", "JavaScript")]

for text, value in radiobuttons:
    tk.Radiobutton(root, text = text, variable = var, value = value).pack(anchor = "w")

root.mainloop()
