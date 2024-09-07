passcode = "passcode"
count = 0

while (count<3):
    userpasscode = str(input("Enter passcode: "))
    if (userpasscode == passcode):
        print ("Access granted.")
        break
    else:
        print("Wrong passcode.")
        count = count + 1
