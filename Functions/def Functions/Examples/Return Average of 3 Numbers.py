### Return the average of 3 numbers ###

# Calculate average and print result outside function
def avgnum():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    num3 = int(input("Enter number 3: "))
    sum = num1 + num2 + num3
    avg = sum/3
    return (avg)

avg1 = avgnum()
print (avg1)
