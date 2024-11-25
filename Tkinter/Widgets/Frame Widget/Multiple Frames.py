### Multiple Frame Widgets ###

import tkinter as tk
root = tk.Tk()
root.title("Frame Widget")
root.geometry("600x400")

# Frame widget
lframe = tk.Frame(root, bd=5, relief="solid")
lframe.pack(side="left", padx=10, pady=10)

Llabel = tk.Label(lframe, text="This is a label inside a frame").pack(padx=15, pady=15)
Lbutton = tk.Button(lframe, text="Button 1").pack(padx=15, pady=15)

# Frame widget
rframe = tk.Frame(root, bd=5, relief="groove")
rframe.pack(side="right", padx=10, pady=10)

Rlabel = tk.Label(rframe, text="This is a label inside a frame").pack(padx=15, pady=15)
Rbutton = tk.Button(rframe, text="Button 2").pack(padx=15, pady=15)

root.mainloop()
