### Functions - Keyword Arguments ###


def cal_area(len, wid):
    area = len * wid
    return area

rectangle = cal_area(len = 5, wid = 11)
print (rectangle) # Output: 55


def stu_info(name, rollno):
    print (name)
    print (rollno)

stu_info ("Riya", 1)
'''
Output:
Riya
1
'''
stu_info (name = "Sneha", rollno = 3)
'''
Output:
Sneha
3
'''
stu_info (rollno = 4, name = "Vaibhavi")
'''
Output:
Vaibhavi
4
'''
