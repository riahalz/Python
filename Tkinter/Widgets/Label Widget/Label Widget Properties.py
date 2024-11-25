### Label Widget Properties ###

import tkinter as tk
root = tk.Tk()
root.title("tkinter properties")
root.geometry("800x600")
root.resizable(True, True)

# Create Label
label = tk.Label(
    root,
    height = 10,
    width = 50,
    # text - text on the label
    text = "Hello All! This is some text inside a label with various properties.",
    # font - font styles
    font = ("Arial", 16, "italic", "underline"),
    # bg - background color of label
    bg = "yellow",
    # fg - foreground/content color of label
    fg = "green",
    # padx, pady - vertical and horizontal padding
    padx = 10, pady = 10,
    # highlightcolor - color when the label is focused on
    highlightcolor = "violet",
    # relief - 3D appearance of label's border - RIDGE/RAISED/SUNKEN/GROOVE/FLAT
    relief = tk.RAISED,
    # borderwidth - border width/bd/thickness
    borderwidth = 5,
    # anchor - position of text in label (CENTER, N, S, E, W, NW, NW, SW, SE)
    anchor = tk.NE,
    # state - NORMAL/DISABLED
    state = tk.NORMAL,
    # wraplength - text wrapping at specific number of pixels
    wraplength = 150,
    # cursor - style of mouse cursor when hovering over the label
    cursor = "box_spiral",
    # takefocus - allows the label to take keyboard focus
    takefocus = 0
    )
label.pack(pady = 20)

root.mainloop()
