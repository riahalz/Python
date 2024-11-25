### Messagebox Widget ###

import tkinter as tk
# import messagebox module
from tkinter import messagebox as mb
root = tk.Tk()
root.title("Messagebox Widget")
root.geometry("800x600")
root.resizable(True, True)

def show_msgbox():
    mb.showinfo("Message", "Button Clicked")

button = tk.Button(root,
                 text = "Click to display a message",
                 command = show_msgbox,
                 )
button.pack(padx = 20, pady = 20)
                 
# askokcancel(title, message, options)

# askquestion(title, message, options)

# askretrycancel(title, message, options)

# askyesno(title, message, options)

# askyesnocancel(title, message, options)

# showerror(title, message, options)

# showinfo(title, message, options)

# showwarning(title, message, options)

root.mainloop()
