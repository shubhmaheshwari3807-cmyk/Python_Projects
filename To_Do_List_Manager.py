with open("todolist.txt", "a") as f:
    times=int(input("How many points do you want to enter: "))
    i=0
    while i<times:
        print(">", end=" ")
        f.write(input("").capitalize() + "\n")
        i+=1

answer=input("Do you want to see the list: ")
if(answer.lower()=="yes" or answer.lower()=="y"):
    with open("todolist.txt", "r") as f:
        while True:
            line=f.readline()
            if(line==""):
                break
            print(line, end="")
elif(answer.lower()=="no" or answer.lower()=='n'):
    print("The list is not printed")

answer_one=input("Do you want to delete the list: ")
if(answer_one.lower()=="yes" or answer_one.lower()=="y"):
    import os
    os.remove("todolist.txt")
if(answer_one.lower()=="no" or answer_one.lower()=="n"):
    print("The list is not deleted")
