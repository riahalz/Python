### Calculate sum of digits in a number ###

def sumdigits(num):
    sum = 0
    for digit in num:
        sum += int(digit)
    print (sum)
        
num = input("Enter a  number: ")
sumdigits(num)
