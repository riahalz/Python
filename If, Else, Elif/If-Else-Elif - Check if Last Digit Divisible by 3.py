n = int(input("Enter a number: "))
ld = int(repr(n)[-1])

if (ld%3)==0:
    print (ld, " is divisible by 3")
else:
    print (ld, " is not divisible by 3")
    
