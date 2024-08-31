### Convert decimal to binary number ###

n = int(input("Enter a positive number: "))
bin = 0
p = 1

while n>0:
    rem = int(n%2)
    bin = bin+rem*p
    p = p*10
    n = n/2

print("Binary number = ", bin)
        
