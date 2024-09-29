### bit_length() function - Returns Length of Binary Conversion of Number ###


def string_bit_length(string):
    return len(string.encode('utf-8')) * 8

my_string = "Hello, World!"

# bit_length function
bit_length = string_bit_length(my_string)

print(bit_length) 

