### Login - Username and Password ###

import tkinter as tk
root = tk.Tk()
root.title("Login - Username and Password")
root.geometry("600x400")

userid = 'admin'
password = '12345'

def login():
    entry1.get()
    entry2.get()
    if entry1.get()==userid and entry2.get()==password:
        label3.config(text="Login Successful")
    else:
        label3.config(text="Login Failed")

label1 = tk.Label(root, text="Enter your username:", font=("Arial", 16))
label1.pack()
entry1 = tk.Entry(root, font=("Arial", 16))
entry1.pack()

label2 = tk.Label(root, text="Enter your password:", font=("Arial", 16))
label2.pack()
entry2 = tk.Entry(root, font=("Arial", 16))
entry2.pack()

label3 = tk.Label(root, font=("Arial", 16))
label3.pack()

button = tk.Button(root, text="Login", font=("Arial", 16), command=login)
button.pack()

root.mainloop()
