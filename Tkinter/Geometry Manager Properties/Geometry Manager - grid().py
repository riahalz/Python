### geometry manager - grid() ###

from tkinter import *
root = Tk()
root.title("Geometry Manager - grid()")
root.geometry("600x400")
root.resizable(True, True)

# Create widgets
myLabel = Label(root, text = "Hello")
myLabel2 = Label(root, text = "Good Morning")

# grid() - places widgets in grid
myLabel.grid(row = 0, column = 0)
myLabel2.grid(row = 5, column = 5)

root.mainloop()
