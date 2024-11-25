### Warning Messagebox ###

import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Warning Messagebox")
root.geometry("800x600")
root.resizable(True, True)

def show_warning():
    result = messagebox.askyesno(
        title = "Warning",
        message = "Do you want to proceed?",)
    if result:
        messagebox.showinfo(
            "Result",
            "You agreed to proceed")
    else:
        messagebox.showinfo(
            "Result",
            "You did not agree to proceed")
        
button = tk.Button(root,
                 text = "Show Warning",
                 command = show_warning
                 )
button.pack(padx = 20, pady = 20)
                 
root.mainloop
