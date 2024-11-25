### Hover Effect ###

import tkinter as tk

def example():
    root = tk.Tk()
    root.title("Hover Effect")
    root.geometry = ("800x600")

    def on_enter(e):
        e.widget['bg'] = 'pink'

    def on_leave(e):
        e.widget['bg'] = 'SystemButtonFace'

    button = tk.Button(root, text = "Hover over this button")
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    button.pack(pady = 20)
                        
    root.mainloop()

example()
