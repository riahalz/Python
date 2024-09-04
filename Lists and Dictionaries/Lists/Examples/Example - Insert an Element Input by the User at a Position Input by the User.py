### Lists - Example - Insert an Element Input by the User at a Position Input by the User ######

list = [12,34,"AA","SD"]

print (list)

n = str(input("Enter an element that you want to be inserted into the list: "))
pos = int(input("Enter the index where you want the element to be inserted: "))

list.insert(pos,n)


print (list)
