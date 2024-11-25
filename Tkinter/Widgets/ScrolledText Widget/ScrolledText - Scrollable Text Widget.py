### ScrolledText - Scrollbar in Text Widget ###

import tkinter as tk
from tkinter import scrolledtext
root = tk.Tk()
root.title("ScrolledText - Scrollbar in Text Widget")
root.geometry("600x400")

# create scrollable text box widget
scrolltext = scrolledtext.ScrolledText(root, height = 10, width = 50, font = "courier", bg = "yellow")
scrolltext.pack()

root.mainloop()
