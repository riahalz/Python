### Button Widget Properties ###

import tkinter as tk
root = tk.Tk()
root.title("Button Widget Properties")
root.geometry("800x600")
root.resizable(True, True)

def on_click():
    print("Button clicked")
    
# Create Button
button = tk.Button(root,
                   # height of button
                   height = 8,
                   # width of button
                   width = 15,
                   # text - text displayed on the button
                   text = "Click this Button",
                   # command - name of function to be executed when button is clicked
                   command = on_click,
                   # font - font styles
                   font = ("Arial", 20, "italic"),
                   # bg - background color of widget
                   bg = "lightblue",
                   # fg - foreground/text color of button
                   fg = "black",
                   # borderwidth/bd - border width/thickness
                   bd = 5,
                   # anchor - position of text in button (CENTER, N, S, E, W, NW, NW, SW, SE)
                   anchor = tk.NE,
                   # activebackground - background color of button when focused on
                   activebackground = "yellow",
                   # activeforeground - foreground color of button when focused on
                   activeforeground = "orange",
                   # padx - horizontal padding
                   padx = 10,
                   # pady - vertical padding
                   pady = 10,
                   # highlightbackground - color of focus highlight when button is not focused on
                   highlightbackground = "green",
                   # highlightcolor - color of focus highlight when button is focused on
                   highlightcolor = "pink",
                   # highlightthickness - thickness of the focus highlight
                   highlightthickness = 3,
                   # relief - 3D appearance of button's border - RIDGE, RAISED, SUNKEN, GROOVE, FLAT
                   relief = tk.RAISED,
                   # state - NORMAL/DISABLED
                   state = tk.NORMAL,
                   # wraplength - text wrapping at specific number of pixels
                   wraplength = 130,
                   # underline - underlines character of button's text (default = -1, no character underlined)
                   underline = 1,
                   # cursor - style of mouse cursor when hovering over the button
                   cursor = "box_spiral",
                   # takefocus - allows the button to take keyboard focus (ex: spacebar pressed means button clicked)
                   takefocus = 0
                   )
button.pack(pady = 20)

root.mainloop()
