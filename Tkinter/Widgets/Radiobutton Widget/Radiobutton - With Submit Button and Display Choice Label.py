### Radiobutton - Submit Choice ###

import tkinter as tk

def submit_choice():
    label.config(text = f"You chose: {var.get()}")

root = tk.Tk()
root.title("Radiobutton - Submit Choice")
root.geometry("400x200")

# create a Tkinter variable
var = tk.StringVar(value = "Option 1") # set option value 

# create radio button widgets
radio1 = tk.Radiobutton(root, text = "Option 1", variable = var, value = "Option 1")
radio1.pack()

radio2 = tk.Radiobutton(root, text = "Option 2", variable = var, value = "Option 2")
radio2.pack()

# create label widget
label = tk.Label(root, text = "Selected: Option 1")
label.pack()

# create button widget
button = tk.Button(root, text = "Submit", command = submit_choice)
button.pack()

root.mainloop()
