### Simple calculator ###

# Functions for operations
def add(num1, num2):
    print (num1 + num2)

def subtract(num1, num2):
    print (num1 - num2)

def multiply(num1, num2):
    print (num1 * num2)

def divide(num1, num2):
    print (num1 / num2)

print("Select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

# Take input from user
select = int(input("Select operation number: "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if select == 1:
    add(num1, num2)
elif select == 2:
    subtract(num1, num2)
elif select == 3:
    multiply(num1, num2)
elif select == 4:
    divide(num1, num2)
else:
    print("Invalid input")
