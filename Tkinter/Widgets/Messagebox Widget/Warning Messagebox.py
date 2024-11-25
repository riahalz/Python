### Warning Messagebox ###

import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Warning Messagebox")
root.geometry("800x600")
root.resizable(True, True)

# Function to display warning messagebox
def ask_question():
    result = messagebox.askyesno(
        title = "Confirmation",
        message = "Do you want to proceed?",
        icon = 'question')
    # If clicked Yes, display message
    if result:
        messagebox.showinfo(
            "Result",
            "You clicked Yes")
    # If clicked No, display message
    else:
        messagebox.showinfo(
            "Result",
            "You clicked No")
        
button = tk.Button(root,
                 text = "Ask Question",
                 command = ask_question
                 )
button.pack(padx = 20, pady = 20)
                 
root.mainloop
