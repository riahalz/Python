### ljust, rjust, center - Fill string of specific width with characters ###


## ljust - adds characters to left of string of specified length
str = "Awesome"
# ljust (width, fillchar)
str.ljust(12, "#")
print (str.ljust(12, "#"))
# Output: Awesome#####


## rjust - adds characters to right of string of specified length
str2 = "Awesome"
# rjust (width, fillchar)
str2.rjust(22," ")
print(str2.center(22, " "))
# Output:        Awesome        


## center - adds characters to center of specified length
str3 = "Python"
# center (width, fillchar)
str3.center(15, "-")
print(str3.center(15, "-"))
# Output: -----Python----
