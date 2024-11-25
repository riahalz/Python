### Combobox Widget with Command ###

import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Combobox Widget with Command")
root.geometry("400x200")

# define function - on selecting a color
def on_select():
    selected = combobox.get()
    # if combobox input is not in list 'options', display a message to select valid input
    if selected not in options:
        resultlabel.config(text = "Please select one of the provided options")
    # if combobox input is in list 'options', display message of selected color
    else:
        resultlabel.config(text = f"You selected: {selected}")

# create Label widget 
label = ttk.Label(root, text = "Select your favorite color")
label.pack()

# create Combobox widget with options and command
options = ["Blue", "Green", "Red", "Black", "White"]
combobox = ttk.Combobox(root, values = options)
combobox.set("Select a color")
combobox.pack()

# create Button widget with command
button = ttk.Button(root, text = "Submit", command = on_select)
button.pack()

# create Result Label widget 
resultlabel = ttk.Label(root, text = "No color selected")
resultlabel.pack()

root.mainloop()
