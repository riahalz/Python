### Text Input/Entry Widget ###
 
import tkinter as tk
root = tk.Tk()
root.title("Text Input/Entry Widget")
root.geometry("600x400")

# Create text input/entry widget
entry = tk.Entry(root, width = 50)

# Place the widget on the screen
entry.pack()

root.mainloop()
