### Try-Except-Finally Statements - Multiple Except Statements in 1 Except Block ###


num = [5, 6, 'a', 7, 8, 9]
b = 15
for x in num:
    try:
        c = b/x
        print (c)
    except ZeroDivisionError:
        print("Cannot be divided by 0")
    except TypeError:
        print ("Enter only integer value")
