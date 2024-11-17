### map() function ###

a = [1, 2, 4, 6, 9, 12]

# map(function, iterable)
b = map(lambda x: x*3, a)

print(list(b))
''' Output: [3, 6, 12, 18, 27, 36] '''
