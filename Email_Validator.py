email=input("Enter your email: ")
if(email.endswith(".com") and email.count("@")==1):
    print("Valid email")
else:
    print("Invalid email")
