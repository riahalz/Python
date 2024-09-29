### enumerate() operator -  ###


## Display index along with element
fruits = ['apple', 'orange', 'mango']
# enumerate() operator
for item in enumerate(fruits):
    print("Index:", item[0], "Fruit", item[1])

'''
Output:
Index: 0 Fruit apple
Index: 1 Fruit orange
Index: 2 Fruit mango
'''

## Display list name along with index and element
veggies = ['carrot', 'brocolli', 'spinach']
for item in enumerate(veggies, 1):
    print ("Veggies#" + str(item[0]) + " : " + item[1])
    
'''
Output:
Veggies#1 : carrot
Veggies#2 : brocolli
Veggies#3 : spinach
'''
