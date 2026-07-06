with open("Notes.txt", "a") as f:
    times=int(input("How many notes do you want to enter: "))
    i=0
    while i<times:
        note=input("Enter the note: ").capitalize()
        f.write(note + "\n")
        i+=1

with open("Notes.txt", "r") as f:
    print(f.read())