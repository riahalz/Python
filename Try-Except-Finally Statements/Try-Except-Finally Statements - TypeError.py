### Try-Except-Finally Statements - TypeError ###


num = [5, 6, 'a', 7, 8, 9]
b = 15
for x in num:
    try:
        c = b/x
        print (c)
    except ZeroDivisionError:
        print("Cannot be divided by 0")
    # If value is not an integer, show TypeError
    except TypeError:
        print ("Enter only integer value")
