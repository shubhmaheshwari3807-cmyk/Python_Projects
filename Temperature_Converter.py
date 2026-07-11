temp=float(input("Enter temperature: "))
question=input("What unit you have chosen (F/C): ")

if(question=="F" or question=="f"):
    celsius= ((temp-32)*5)/9

    print("Your temperature is", celsius, "in degree celsius")

elif(question=="C" or question=="c"):
    Fahr= ((temp*9)/5)+32

    print("Your temperature is", Fahr, "in degree fahrenheit")
else:
    print("Invalid Input")
