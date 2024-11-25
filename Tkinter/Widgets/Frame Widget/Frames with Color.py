### Frames with Color ###

import tkinter as tk
root = tk.Tk()
root.title("Frames with Color")
root.geometry("800x600")
root.resizable(True, True)

colors = ['red', 'blue', 'green', 'orange']
for color in colors:
    frame = tk.Frame (
        root,
        height = 500,
        width = 900,
        )
    frame.pack(pady=5)
    tk.Label(
        frame,
        text = f"{color.title()}Frame",
        bg = color
        ).pack(pady=10)

root.mainloop
