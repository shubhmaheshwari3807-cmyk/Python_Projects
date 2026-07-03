count=0
password="python123"
attempt=input("Enter the Password: ")
while attempt!=password and count<2:
    print("Incorrect Password")
    count+=1
    print("Attempt", count, "failed")
    attempt=input("Enter the Password: ")
if(attempt==password):
    print("Correct Password")
else:
    print("Locked Out")
    