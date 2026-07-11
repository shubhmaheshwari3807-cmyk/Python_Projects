import random
print("------Welcome To Random Number Game------")
ranNum=random.randint(0, 100)
attempt=0
print(ranNum)
while True:
    guess=int(input("Enter your guess: "))
    if(guess==ranNum):
        print("------You Won------")
        print("You guessed the number")
        print("------Game Over------")
        attempt+=1
        print("You won in ", attempt, "attempt")
        break 
    elif(guess<ranNum):
        print("------Try Again------")
        print("Your guess was smaller than the number. Guess Again")
        attempt+=1
        print("Your attempt number ", attempt)
    else:
        print("------Try Again------")
        print("Your guess was larger than the number. Guess Again")
        attempt+=1
        print("Your attempt number ", attempt)
    if(attempt==5):
        print("Your Reached Your Limit")
        print("------You Lose------")
        break