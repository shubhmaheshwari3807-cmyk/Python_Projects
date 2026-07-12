secret=67
number=int(input("Enter your guess: "))
while number!=secret:
    if(number>75):
        print("The number you have chosen is too high")
    elif(number<=50):
        print("The number you have chosen is too low")
    number=int(input("Incorrect guess" + "\n" + "Enter your guess:"+ " "))
if(number==secret):
    print("You have gussed the number")
