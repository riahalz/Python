### isnumeric(), isdecimal(), isdigit(), isidentifier() - Check String Value Type ###


## isnumeric() - Check if string contains numeric characters or not
str = "12134"
# isnumeric()
str.isnumeric()
print (str.isnumeric())
# Output: True

str2 = "Awesome"
str2.isnumeric()
print (str2.isnumeric())
# Output: False


## isdecimal() - Check if string is a decimal or not
str3 = "123.45"
# isdecimal()
str3.isdecimal()
print (str3.isdecimal())
# Output: False


## isdigit() - Check if string is a digit/contains only digits or not
str4 = "45"
str4.isdigit()
print (str4.isdigit())
# Output: True

print("45.5".isdigit())
# Output: False


## isidentifier() - Check if string is an identifier or not

str5 = "str"
# isidentifier()
str5.isidentifier()
print (str5.isidentifier())
# Output: True

print ("1str%".isidentifier())
# Output: False
