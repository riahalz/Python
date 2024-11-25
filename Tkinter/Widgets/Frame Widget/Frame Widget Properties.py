### Frame Widget Properties ###

import tkinter as tk
root = tk.Tk()
root.title("Frame Widget Properties")
root.geometry("600x300")
root.resizable(True, True)
          
# Frame
frame = tk.Frame(
    root,
    # height of frame
    height = 100,
    # width of frame
    width = 400,
    # bg - background color of widget
    bg = "green",
    # relief - 3D appearance of frame's border - RIDGE, RAISED, SUNKEN, GROOVE, FLAT
    relief = tk.RIDGE,
    # borderwidth/bd - border width/thickness (default = 2)
    bd = 5,
    # cursor - changes the mouse cursor when hovering over the widget
    cursor = "arrow",
    # highlightbackground - color of focus highlight when frame is not focused on
    highlightbackground = "yellow",
    # highlightcolor - color of focus highlight when frame is focused on
    highlightcolor = "blue",
    # highlightthickness - thickness of the focus highlight
    highlightthickness = 5,
    )

# Add frame widget to screen
frame.pack(pady = 20)

root.mainloop()
