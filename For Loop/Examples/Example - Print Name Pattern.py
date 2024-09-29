### for loop - Display Name entered by user adding 1 letter each time ###

name = str(input("Enter your name: "))

for i in range (len(name) + 1):
    for letter in range(i):
        print (name[letter], end = " ")
    print ()

