### Lists - Deleting Values in a List ###


list = [1,2,3,4,5,6,7,8]


# Deleting 1 value in the list

del (list[5])

print (list) # Output: [1, 2, 3, 4, 5, 7, 8]


# Deleting a range of values in the list

del (list[2:5])

print (list) # Output: [1, 2, 7, 8]


# Deleting the entire list

del list

# Verify list has been deleted and does not get printed
print (list) # Output: <class 'list'>


