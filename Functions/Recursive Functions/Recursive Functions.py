### Recursive Functions ###
# Calling a function within the function repeatedly

# Example - Find factorial of a number
def factorial(n):
    if (n==1):
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter a number: "))
result = factorial(n)
print (result)

print (factorial(5)) # Output: 120
print (factorial(9)) # Output: 362880
