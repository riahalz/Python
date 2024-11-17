### Calculate the area of a rectangle ###

# with single def function
def area():
    length = int(input("Enter length: "))
    breadth = int(input("Enter breadth: "))
    area = length * breadth
    return (area)

area1 = area()
print (area1)

## with 2 def functions
def getlb():
    length = int(input("Enter length: "))
    breadth = int(input("Enter breadth: "))
    area(length, breadth)

def area(length, breadth):
    area1 = length * breadth
    print (area1)

getlb()

