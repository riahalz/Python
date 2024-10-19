### Create function calculation() such that it accepts 2 variables and calculates sum and subtraction and returns both values in a single return cell ### ###


def calculation(x, y):
    sum = x + y
    if x > y:
        diff = x - y
    else:
        diff = y -x
    return (sum, diff)

x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
print (calculation(x, y)) # Output: sum, diff 
