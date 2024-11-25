### Multiline Text Entry Widget ###
 
import tkinter as tk
root = tk.Tk()
root.title("Multiline Text Entry Widget")
root.geometry("600x400")

# Create multiline text entry widget
text_area = tk.Text(root, height = 20, width = 40, font = "Courier")

# Place the widget on the screen
text_area.pack()

root.mainloop()
