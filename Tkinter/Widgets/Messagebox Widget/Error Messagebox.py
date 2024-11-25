### Error Messagebox ###

import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Error Messagebox")
root.geometry("800x600")
root.resizable(True, True)

def show_error():
    messagebox.showerror (
        title = "Error",
        message = "An error occurred")

button = tk.Button(root,
                 text = "Click to display a message",
                 command = show_error
                 )
button.pack(padx = 20, pady = 20)

root.mainloop
