### Index() - Find Index of Element in String ###


str = "Hello to the world"

## find index of element using index()
str.index("the")
# This includes the black spaces in the string

print (str.index("the"))
# Output: 9

print (str.index("to"))
# Output: 6

print (str.index("world"))
# Output: 1


# Element not present in string - error
print (str.index("as"))
# Output: ValueError: substring not found
