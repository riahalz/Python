### Find the maximum among 3 numbers ###

def maxnums(n1, n2, n3):
    if n1 > n2:
        if n1 > n3:
            print (n1)
    elif n2 > n1:
        if n2 > n3:
            print (n2)
    else:
        print (n3)

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
maxnums(n1, n2, n3)
