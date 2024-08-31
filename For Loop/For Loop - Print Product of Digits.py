### for loop - Find product of digits of a number entered by user ###

n = int(input("Enter a number: "))

# Define a function for calculating product of digits
def ProductOfDigits(n): 
    product = 1 # let product = 1
    # Convert number into string for counting digits
    for digit in str(n):  
      product *= int(digit)       
    return product

print(ProductOfDigits(n))
