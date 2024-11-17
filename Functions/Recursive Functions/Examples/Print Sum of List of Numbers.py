### Return sum of list of numbers ###

def sumlist(list):
    if not list:
        return 0
    else:
        return list[0] + sumlist(list[1:])

print (sumlist([2, 6, 9, 10])) # Output: 27
