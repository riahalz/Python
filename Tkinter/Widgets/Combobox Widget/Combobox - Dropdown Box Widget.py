### Combobox - Dropdown Box Widget ###

import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Combobox - Dropdown Box Widget")
root.geometry("400x200")

# create Combobox widget with options
options = ["Option 1", "Option 2", "Option 3", "Option 4"]
combobox = ttk.Combobox(root, values = options)
combobox.pack()

root.mainloop()


