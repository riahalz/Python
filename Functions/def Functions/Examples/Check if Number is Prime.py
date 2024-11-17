### Check if Number is Prime ###

def is_prime(num):
    # Prime numbers are greater than 1
    if num <= 1:
        return False
    # Check for factors from 2 to square root of number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Get number from user
number = int(input("Enter a number to check if it's prime: "))

# Check if number is prime and display result
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
