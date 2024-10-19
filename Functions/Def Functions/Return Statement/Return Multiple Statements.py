### Return Multiple Statements ###

def multi_return(x):
    if x>0:
        return "Positive"
    elif x<0:
        return "Negative"
    else:
        return "Zero"

# print the results for various values of x
print (multi_return(5)) # Output: Positive
print (multi_return(-6)) # Output: Negative
print (multi_return(0)) # Output: Zero

