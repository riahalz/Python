### Text Widget Properties ###
 
import tkinter as tk
root = tk.Tk()
root.title("Text Widget Properties")
root.geometry("600x400")

# Text widget
text_area = tk.Text(root,
                    height = 20,
                    width = 40,
                    # bg - background color
                    bg = "green",
                    # fg - foreground color
                    fg = "white",
                    # font - font styles
                    font = ("Courier", 20, "italic"),
                    # padx - padding added to left and right of widget
                    padx = 5,
                    # pady - padding added to top and bottom of widget
                    pady = 5,
                    # highlightbackground - color of focus highlight when widget is not focused on
                    highlightbackground = "blue",
                    # highlightcolor - color of focus highlight when widget is focused on
                    highlightcolor = "pink",
                    # highlightthickness - thickness of the focus highlight
                    highlightthickness = 2,
                    # insertbackground - color of the insertion cursor (default - black)
                    insertbackground = "violet",
                    # selectbackground - background color used to display selected text
                    selectbackground = "orange",
                    # state - NORMAL, DISABLED
                    state = tk.NORMAL,
                    # relief - 3D appearance of widget - SUNKEN, RAISED, FLAT, RIDGE, GROOVE
                    relief = tk.RAISED,
                    # cursor - style of mouse cursor when hovering over the widget
                    cursor = "arrow",
                    # exportselection - text exported to be the selection in the window manager
                    exportselection = 0,
                    # insertofftime - number of milliseconds the insertion cursor is off during its blink cycle
                    insertofftime = 120,
                    # insertontime - number of milliseconds the insertion cursor is on during its blink cycle
                    insertontime = 400,
                    # insertwidth - width of insertion cursor (default - 2px)
                    insertwidth = 3,
                    # insertborderwidth - width of border around insertion cursor
                    insertborderwidth = 2,
                    # wrap - wrapping of text in widget (CHAR, WORD)
                    wrap = tk.WORD,
                    # bd - border width/thickness
                    bd = 5,
                    )

# Place the widget on the screen
text_area.pack()

root.mainloop()
