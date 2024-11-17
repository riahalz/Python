### Calculate area of triangle and circle ###

# get values of radius, base, height
def getdata():
    r = int(input("Input radius: "))
    b = int(input("Input base length: "))
    h = int(input("Input height: "))
    area_triangle(b, h)
    area_circle(r)

# area of triangle
def area_triangle(b, h):
    areatri = (1/2)*b*h
    print (areatri)

# area of circle
def area_circle(r):
    areacir = (22/7) * (r*r)
    print (areacir)

getdata()

'''
Output:
Input radius: r
Input base length: b
Input height: h
areatri
areacir
'''
