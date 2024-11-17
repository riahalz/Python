### Recursive Function - Walking Steps ###

def walk(steps):
    if steps == 0:
        return
    print(f"You took step #{steps}")
    walk(steps - 1)

walk(10)

''' Output:
You took step #10
You took step #9
You took step #8
You took step #7
You took step #6
You took step #5
You took step #4
You took step #3
You took step #2
You took step #1
'''
