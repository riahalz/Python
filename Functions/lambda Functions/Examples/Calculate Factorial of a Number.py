### Calculate factorial of a number ###

factorial = lambda x: x * factorial(x-1) if (x>1) else 1

print(factorial(6))
''' Output: 720 '''
