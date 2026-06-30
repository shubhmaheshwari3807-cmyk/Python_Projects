correct_name="Shubh"
correct_password="python123"

name=input("Enter the correct name: ")
if(name!=correct_name):
    print("Invalid Credentials Entered\nLogin Unsuccessful")
else:
    password=input("Enter the correct password: ")
    if(password!=correct_password):
        print("Invalid Credentials Entered\nLogin Unsuccessful")
    else:
        print("Login Successful")

