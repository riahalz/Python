### Functions ###


## def function_name() - define a function
def greet():
    # statement(s)
    print ("Hello world")
    print ("Welcome to Python programming")
    # return statement - returns value from the function (optional)
    return

# call the function
greet()

'''
Output: Hello world
Welcome to Python programming
'''


## define a function with a specific value as parameter
def greet(name):
    print ("Hello", name)
    print ("Welcome to Python programming")

# call the function with the specific value as parameter
greet("Riya")

'''
Output:
Hello Riya
Welcome to Python programming
'''

## define a function with a specific value to be input as parameter
def greet(name):
    print ("Hello", name)
    print ("Welcome to Python programming")

# call the function with the specific value as parameter
name = input("Enter your name: ")
greet(name)

'''
Output:
Hello (name)
Welcome to Python programming
'''
