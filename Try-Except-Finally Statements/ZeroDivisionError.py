### Try-Except-Finally Statements - ZeroDivisionError ###


try:
    numerator = int(input("Enter numerator value: "))
    denominator = int(input("Enter denominator value: "))
    result = numerator/denominator
    print (result)

# If denominator = 0, show ZeroDivisionError
except ZeroDivisionError:
    print("Denominator cannot be 0")
    
