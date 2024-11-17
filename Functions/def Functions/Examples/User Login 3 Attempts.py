### User Login - 3 Attempts ###

passcode = "PesU@1"
id1 = "ADMIN"

def login():
    count = 0
    while (count<3):
        userid = input("Enter user id: ")
        userpasscode = input("Enter passcode: ")
        if (userpasscode == passcode) and (userid == id1):
            print ("Login Successful.")
            break
        else:
            print("Wrong passcode.")
            count = count + 1
        if count == 3:
            print ("Account Blocked")

login()
