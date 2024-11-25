### Label widget with image ###

import tkinter as tk
root = tk.Tk()
root.title("Label Widget with Image")
root.geometry("800x600")
root.resizable(True, True)

# Create Label widget
label = tk.Label(
    root,
    height = 10,
    width = 50,
    text = "H",
    # image
    )
label.pack(pady = 20)

root.mainloop()
