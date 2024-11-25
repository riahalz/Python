### Frame with Button Click Counter ###

import tkinter as tk
root = tk.Tk()
root.title("Frame with Button Click Counter")
root.geometry("600x400")

counter1 = 0
def inc_counter1():
    global counter1
    counter1 += 1
    button1.config(text=str(counter1))
    print("Button 1 clicked")

counter2 = 0
def inc_counter2():
    global counter2
    counter2 += 1
    button2.config(text=str(counter2))
    print("Button 2 clicked")

counter3 = 0
def inc_counter3():
    global counter3
    counter3 += 1
    button3.config(text=str(counter3))
    print("Button 3 clicked")

frame = tk.Frame(root, bd=5, relief="groove")
frame.pack()

button1 = tk.Button(frame,
                   text=str(counter1),
                   width=15,
                   font=("Arial", 16),
                   command=inc_counter1)

button1.pack(pady=20)

button2 = tk.Button(frame,
                   text=str(counter2),
                   width=30,
                   font=("Arial", 16),
                   command=inc_counter2)

button2.pack(pady=20)

button3 = tk.Button(frame,
                   text=str(counter3),
                   width=15,
                   font=("Arial", 16),
                   command=inc_counter3)

button3.pack(pady=20)

root.mainloop()
