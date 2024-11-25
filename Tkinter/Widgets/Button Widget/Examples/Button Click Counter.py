### Button Click Counter ###

import tkinter as tk
root = tk.Tk()
root.title("Counter Button")
root.geometry("600x400")

# define counter = 0 initially
counter
= 0

# function to increment counter each time button is clicked
def inc_counter():
    global counter
    counter += 1
    button.config(text=str(counter))

# create button
button = tk.Button(root,
                   text=str(counter),
                   width=15,
                   font=("Arial", 16),
                   command=inc_counter)
button.pack(pady=20)

root.mainloop()
