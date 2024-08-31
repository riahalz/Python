### for loop - Find product of digits of a number entered by user ###

n = int(input("Enter a number: "))

p=0
for i in (n):
    p = p + int(i)**3
if int(n)==p:
    print("Number is an Armstrong number")
else:
    print("Number is not an Armstrong number")
