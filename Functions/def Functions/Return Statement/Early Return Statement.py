### Early Return ###

def early_return(lst):
    if not lst:
        return None
    total = sum(lst)
    return total

print (early_return([])) # Output: None
print (early_return([1, 3, 4])) # Output: 8
