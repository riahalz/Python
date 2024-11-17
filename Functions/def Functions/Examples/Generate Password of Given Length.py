### Generate a password of a given length ###

import random
import string

def generate_password(length):
    # Characters to choose from: uppercase, lowercase, digits, special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate random password of the given length
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Get password length from user
length = int(input("Enter your desired password length: "))
# Generate and display password
password = generate_password(length)
print("Generated password: ", password)
    
