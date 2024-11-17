### Print Docstrings/Comments in function ###

def greet(name):
    '''This function greets the specified user'''
    print ("Good morning", name)

greet("Riya")

# print docstrings
print(greet.__doc__)

'''
Output:
Good morning Riya
This function greets the specified user
'''
