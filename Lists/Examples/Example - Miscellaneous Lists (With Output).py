### Python - Lists - 3/9/2024 Class Task ###


## Create lists:
Veggies = ["carrot", "potato", "lettuce", "beans", "corn"]
Vowels = ["a", "e", "i", "o", "u"]
NaturalNumbers = [0,1,2,3,4,5,6,7,8,9]
Friends = ["Vaibhavi", "Sneha", "Harini", "Shikha", "Sartaj"]
TajMahal = ["T", "a", "j", " ", "M", "a", "h", "a", "l"]


## Convert "Practice" into list:
word = "Practice"
print (list(word))
# Print a character next to each letter
for i in (word):
    print(i,"#")
    
# Output:
# P #
# r #
# a #
# c #
# t #
# i #
# c #
# e #

## Find output of the following:
d = "a*hj"
list (d)
# Output: ['a', '*', 'h', 'j']


## Convert "String" into list:
a = "String"
list(a)
# Output: ['S', 't', 'r', 'i', 'n', 'g']


## Find output of the following:
a = [1,2,3,4,5]
print(a[0]) # Output: 1
print(a[-1]) # Output: 5
print(a[2]) # Output: 3
print(a[-2]) # Output: 4


## Print all values of the list:
List1 = ['a','b','c','d','e']
for i in (List1):
    print (i)

# Output:
# a
# b
# c
# d
# e

    
## Merge/Concatenate 2 lists:
a = [10,20,30,40,50]
b = [60,70,80,90,100]
print (a + b) # Output: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


## Find output of the following:
list1 = [1,2,3,4,5,6,7,8,9,10]

print (list1 [1:3]) # Output: [2, 3]
print (list1 [6]) # Output: 7
print (list1 [::2]) # Output: [1, 3, 5, 7, 9]
print (list1 [1:5:2]) # Output: [2, 4]
print (list1 [:-4]) # Output: [1, 2, 3, 4, 5, 6]
print (list1 [3:8:-1]) # Output: []


## Find the output of the following code:
mylist = [1,2,3,4,5,6,7,8,9,10]

del mylist[3:]
print (mylist) # Output: [1, 2, 3]

del mylist[:5]
print (mylist) # Output: []

del mylist[:-5]
print (mylist) # Output: []
