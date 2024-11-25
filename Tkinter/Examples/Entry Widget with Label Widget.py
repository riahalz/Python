### Text Entry Widget with Label Widget ###
 
import tkinter as tk
root = tk.Tk()
root.title("Text Entry Widget with Label")
root.geometry("600x400")

# Create label widget
label = tk.Label(root, text = "Enter your name:")

# Create text input/entry widget
entry = tk.Entry(root, width = 50, relief = "raised")

# Place the widgets on the screen
label.pack()
entry.pack()

root.mainloop()
