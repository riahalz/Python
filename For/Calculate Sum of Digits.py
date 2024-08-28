### Find sum of digits of a number entered by user ###

n = int(input("Enter a number: "))

# Define a function for calculating sum of digits
def SumOfDigits(n): 
   
    sum = 0
    # Convert number into string for counting digits
    for digit in str(n):  
      sum += int(digit)       
    return sum

print(SumOfDigits(n))
        
