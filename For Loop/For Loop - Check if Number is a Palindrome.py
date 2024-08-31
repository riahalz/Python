### Check if a number entered by user is a palindrome or not ###

n = int(input("Enter a number: "))

# Define a function for calculating sum of digits
def SumOfDigits(n): 
    sum = 0
    # Convert number into string for counting digits
    for digit in str(n):  
      sum += int(digit)       
    return sum

print(SumOfDigits(n))
