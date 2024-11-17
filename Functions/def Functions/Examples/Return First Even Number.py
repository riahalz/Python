### Find the first even number ###

def find_first_even(number):
    for num in number:
        if num%2 == 0:
            return num
    return None

n1 = [1, 3, 5, 6, 7, 8]
n2 = [1, 3, 5, 7]
print ("First even number in list1: ", find_first_even(n1)) # Output: First even number in list1:  6
print ("First even number in list2: ", find_first_even(n2)) # First even number in list2:  None

