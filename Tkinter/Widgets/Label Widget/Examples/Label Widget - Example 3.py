### Label Widget - Example ###

from tkinter import *
root = Tk()
root.title("Label Widget - Example")
root.geometry("600x400")
root.resizable(True, True)

bold = Label(root,
             text="Bold Text",
             pady=10,
             font=('Arial', 16, 'bold', 'underline'))
bold.pack()

italic = Label(root,
               text="Italic Text",
               pady=10,
               font=('Arial', 16, 'italic'))
italic.pack()

underline = Label(root,
                  text="Underline Text",
                  font=('Arial', 16, 'underline'))
underline.pack(pady=10)

customcolor = Label(root,
                    text="Custom Color",
                    bg="yellow",
                    font=('Arial', 12))
customcolor.pack()

rightalign = Label(root,
                   text="Right Aligned",
                   justify="right",
                   font=('Arial', 12))
rightalign.pack(anchor="e", padx=200, pady=10)

centeralign = Label(root,
                    text="Center Aligned",
                    justify="center",
                    font=('Arial', 12))
centeralign.pack()

button = Button(root,
                text="With Border",
                relief=RIDGE,
                font=('Arial', 12))
button.pack(pady=10)

padded = Label(root,
               text="Padded Text",
               pady=20,
               font=('Arial', 12))
padded.pack()
               

root.mainloop()
