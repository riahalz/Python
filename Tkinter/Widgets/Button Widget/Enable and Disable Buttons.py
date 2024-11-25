### Enable and disable buttons ###

import tkinter as tk

def eg():
    root = tk.Tk()
    root.title("Enable and Disable Buttons")
    root.geometry = ("800x600")

    label = tk.Label(root, text = "Click to toggle button")
    label.pack(pady = 10)

    button1 = tk.Button(root, text = "Toggle Button", command = lambda: button2.config(state = tk.DISABLED if button2['state'] == tk.NORMAL else tk.NORMAL))
    button1.pack(pady = 5)

    button2 = tk.Button(root, text = "Can be disabled", command = lambda: messagebox.showinfo("Button2", "Button2 clicked"))
    button2.pack(pady = 5)
                        
    root.mainloop()

eg()
