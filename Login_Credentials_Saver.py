with open("credentials.txt", "w") as f:
    f.write(input("Enter the username: ") + "\n")
    f.write(input("Enter the password: "))

with open("credentials.txt", "r") as f:
    print(f.read())

answer=input("Do you want to update the credentials: ")
if(answer.lower()=="yes" or answer.lower()=="y"):
    with open("credentials.txt", "w") as f:
        f.write(input("Enter the new username: ") + "\n")
        f.write(input("Enter the new password: "))

elif(answer.lower()=="no" or answer.lower()=="n"):
    print("Your credentials are same as before")
else:
    print("Invalid output")
