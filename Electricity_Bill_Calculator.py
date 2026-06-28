units=int(input("Tell the number of units consumed: "))

if(units>=0 and units<=100):
    bill=50+(3*units)
    print("Your bill is", bill)

elif(units>100 and units<=200):
    bill=50+(5*units)
    print("Your bill is", bill)

elif(units>200 and units<=300):
    bill=50+(7*units)
    print("Your bill is", bill)

elif(units>300):
    bill=50+(10*units)
    print("Your bill is", bill)

else:
    print("Invalid units")