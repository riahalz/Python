### Button Widget - Example ###

from tkinter import *
from tkmacosx import Button
root = Tk()
root.title("Button Widget - Example")
root.geometry("800x600")
root.resizable(True, True)

normal = Button(root,
                   text="Normal Button",
                   state=NORMAL
                   )
normal.pack(pady=5)

disabled = Button(root,
                 text="Disabled Button",
                 state=DISABLED
                   )
disabled.pack(pady=5)

custom = Button(root,
                text="Custom Colors",
                bg='blue'
                   )
custom.pack(pady=5)

wide = Button(root,
              text="Wide Button",
              width=300
                   )
wide.pack(pady=5)

def toggle_button():
    print("Toggle button state")

toggle = Button(root,
                text="Toggle Button State",
                command=toggle_button
                   )
toggle.pack(pady=5)

raised = Button(root,
                text='Raised Relief',
                relief='raised')
raised.pack(pady=5)
                
sunken = Button(root,
                text="Sunken Relief",
                relief ='sunken'
                   )
sunken.pack(pady=5)

ridge = Button(root,
               text="Ridge Relief",
               relief ='ridge'
                   )
ridge.pack(pady=5)

root.mainloop()
