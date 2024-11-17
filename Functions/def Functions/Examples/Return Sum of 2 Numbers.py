### Return the sum of 2 numbers ###

## Calculate sum and print result within function
def sumnum():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    sum = num1 + num2
    print (sum)

sumnum()


## Print result outside function
def sumnum():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    sum = num1 + num2
    return (sum)

# assigning a new variable to call the function
add = sumnum()
print (add)
