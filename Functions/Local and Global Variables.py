### Local and Global Variables ###

def fun1():
    ## local variable - defined inside function
    x = 10
    print ("Value of x inside function: ", x)
    # Output: Value of x inside function:  10

## global variable - defined outside function
x = 20
fun1()
print ("Value of x outside function: ", x)
# Output: Value of x outside function: 20

c = 3
def add():
    # global keyword - to access a global variable
    global c
    c = c + 2
    print ("The modified global variable inside function: ", c)

add()
# Output: The modified global variable inside function: 5
