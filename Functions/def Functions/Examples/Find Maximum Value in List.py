### Find maximum value in List ###

def maxvalue(list):
    list.sort()
    print("Maximum value in the list: ", list[-1])

list = [2, 8, 14, 33]
maxvalue(list)
