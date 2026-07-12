with open("lines.txt", "w") as f:
    times=int(input("How many lines do you want to enter: "))
    i=0
    while i<times:
        line=input("Enter the line: ").capitalize()
        f.write(line + "\n")
        i+=1
with open("lines.txt", "r") as f: 
    j=0
    while j<times:
        print(f.readline(), end="")
        j+=1

with open("lines.txt", "r") as f:
    char=int(input("Enter how many charcters do you want to read: "))
    print(f.read(char))
