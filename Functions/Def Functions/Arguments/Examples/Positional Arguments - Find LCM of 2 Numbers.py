### Positional Arguments - Find LCM of 2 Numbers ###


def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


n1 = 54
n2 = 24
print (lcm(n1, n2)) # Output: 216
