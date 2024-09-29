### Store Roll No.s and Names of Students in Dictionary ###


d = {}

for i in range(5):
    rollno = int(input("Enter roll number: "))
    name = input("Enter name of student: ")
    d[rollno] = name

print (d)
    
