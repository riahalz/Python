### Try-Except-Finally Statements - Check if Even or Odd Number with Else Statement ###


try:
    num = int(input("Enter a number: "))
# if value entered is not an integer, show error
except:
    print ("Enter only an integer value")
else:
    # define a formula for even/odd numbers
    even_or_odd = num%2==0
    # if number is even (even_or_odd = true)
    if even_or_odd:
        print ("Number entered is even")
    # else if number is odd (even_or_odd = false)
    else:
        print ("Number entered is odd")
finally:
    print ("Program executed")
