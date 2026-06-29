current_year=2026
birth_year=int(input("Tell your birth year: "))
age=current_year-birth_year
print("Your age would be", age)
if(birth_year<1928):
    print("Your birth year predates our generation tracking system")
elif(birth_year>=1928 and birth_year<=1945):
    print("You are silent generation")
elif(birth_year>=1946 and birth_year<=1964):
    print("You are a baby boomer")
elif(birth_year>=1965 and birth_year<=1980):
    print("You are generation X")
elif(birth_year>=1981 and birth_year<=1996):
    print("You are a millennial")
elif(birth_year>=1997 and birth_year<=2012):
    print("You are generation Z")
elif(birth_year>=2013 and birth_year<=2026):
    print("you are generation alpha")
elif(birth_year>2026):
    print("Enter appropriate year")