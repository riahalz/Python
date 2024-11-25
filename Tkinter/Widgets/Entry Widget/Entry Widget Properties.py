### Entry Widget Properties ###
 
import tkinter as tk
root = tk.Tk()
root.title("Entry Widget Properties")
root.geometry("600x200")

# Entry widget
text_entry = tk.Entry(root,
                      # width
                      width = 40,
                      # bg - background color
                      bg = "blue",
                      # fg - foreground color
                      fg = "white",
                      # font - font styles
                      font = ("Courier", 20, "italic"),
                      # highlightbackground - color of focus highlight when widget is not focused on
                      highlightbackground = "green",
                      # highlightcolor - color of focus highlight when widget is focused on
                      highlightcolor = "pink",
                      # highlightthickness - thickness of the focus highlight
                      highlightthickness = 2,
                      # insertbackground - color of the insertion cursor (default - black)
                      insertbackground = "violet",
                      # selectbackground - background color used to display selected text
                      selectbackground = "orange",
                      # State - NORMAL, DISABLED
                      state = tk.NORMAL,
                      # relief - 3D appearance of widget - SUNKEN, RAISED, FLAT, RIDGE, GROOVE
                      relief = tk.GROOVE,
                      # cursor - style of mouse cursor when hovering over the widget
                      cursor = "pirate",
                      # exportselection - text exported to be the selection in the window manager
                      exportselection = 0,
                      # insertofftime - number of milliseconds the insertion cursor is off during its blink cycle
                      insertofftime = 100,
                      # insertontime - number of milliseconds the insertion cursor is on during its blink cycle
                      insertontime = 500,
                      # insertwidth - width of insertion cursor (default - 2px)
                      insertwidth = 3,
                      # insertborderwidth - width of border around insertion cursor
                      insertborderwidth = 2,
                      # bd - border width/thickness
                      bd = 5,
                    )

# Place the widget on the screen
text_entry.pack()

root.mainloop()
