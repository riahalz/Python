### tkinter program ###

# import tkinter module
from tkinter import *
# Create main/root window
root = Tk()
# Give a title to the window
root.title("tkinter program")
# Specify dimensions - height and width - of the window
root.geometry("600x400")
# Specify whether window should be resizable or not - height, width
root.resizable(True, True)
# Specify background color
root.config(bg = "lightblue")
# Execute the loop
root.mainloop()
