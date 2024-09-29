### Lists - Accept 10 numbers from the user and display the list. Add new number to the existing list ######

list = []
for i in range (10):
    num = (int(input("Enter a number: ")))
    list.append(num)
print("List elements are: ", list)
print("Insert a new element into the list: ")
n = int(input("Enter a new number: "))
list.append(n)
print ("List after appending new number: ", list)
