### Accept and display employee details - first name, last name, age, department ###


def empdetails(firstname, lastname, age, dept):
    print ("First Name: ", firstname)
    print ("Last Name: ", lastname)
    print ("Age: ", age)
    print ("Department: ", dept)


firstname = input("Enter first name: ")
lastname = input("Enter last name: ")
age = int(input("Enter your age: "))
dept = input("Enter department: ")
empdetails(firstname, lastname, age, dept)
