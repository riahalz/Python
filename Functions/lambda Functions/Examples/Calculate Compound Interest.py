### Calculate compound interest ###

compound = lambda P, R, T, N : ((P*(1+R/N))*(N*T))

P = int(input("Enter principal amount: "))
R = int(input("Enter rate: "))
T = int(input("Enter time (in years): "))
N = int(input("Enter number of times interest is to be compounded: "))

print (compound(P, R, T, N))
