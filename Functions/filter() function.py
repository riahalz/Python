### filter() function ###

a = [2, 3, 7, 11, 6, 18, 23]

# filter(function, iterable)
b = filter(lambda x: x%2==0, a)

print(list(b))
''' Output: [2, 6, 18] '''


