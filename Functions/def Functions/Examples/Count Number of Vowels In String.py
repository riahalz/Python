### Count number of vowels in string ###

def checkvowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in str:
        if i in vowels:
            count += 1
        else:
            continue
    print ("Number of vowels: ", count)
    
str = input("Input a string: ")
checkvowels(str)
