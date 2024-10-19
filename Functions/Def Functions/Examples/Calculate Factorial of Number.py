### Calculate factorial of a number ###

def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    print (result)

num = int(input("Enter a number: "))
factorial(num)
