### Generate list of prime numbers up to a given number ###

def primelist():
    primes = []
    for num in range(2, lim + 1):
        for i in range (2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    print (primes)
            
lim = int(input("Enter the maximum number you want the prime numbers to be generated upto: "))
primelist()
