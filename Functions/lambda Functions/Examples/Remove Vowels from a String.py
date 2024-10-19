### Remove vowels from a string ###

removevowels = lambda str: ''.join([char for char in str if char.lower() not in 'aeiou'])

print (removevowels("Hello world I am here"))
