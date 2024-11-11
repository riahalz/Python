### Calculate power of a number ###

def power(base, exponent):
    return base ** exponent

base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

result = power(base, exponent)
print(result)
