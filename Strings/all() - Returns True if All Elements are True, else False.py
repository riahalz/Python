### all() operator - Returns True if all elements are True, else False ###


a = {'a', 'b', False}
# all() operator
all(a)
print(all(a)) # Output: False

b = [1, 2, 3, 4, 7]
print(all(b)) # Output: True

c = [True, 0, False]
print(all(c)) # Output: False

d = []
print(all(d)) # Output: True

