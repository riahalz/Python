### Count number of 0s in number ###

def countzeros(n):
    if n == 0:
        return 0
    return(True if n % 10 == 0 else 0) + countzeros(n//10)

print (countzeros(10043)) # Output: 2

