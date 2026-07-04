"""def calculate_tax(income, tax_rate):
    income=int(input("Enter your income: "))
    question=input("Do you have tax rate? ")
    if(question=="No" or question =="no" or question=="N" or question=="n"):
        if(income<=1000000):
            tax_rate==0
        elif(income>100000 and income<=500000):
            tax_rate==5
        elif(income>500000):
            tax_rate=10
    elif(question=="Yes" or question=="yes" or question=="Y" or question=="y"):
        tax_rate=int(input("Enter the tax rate: "))
    final_income=income-(income*tax_rate/100)
    print(final_income)

calculate_tax()"""
def calculate_tax(income, tax_rate):
      final_income=income-(income*tax_rate/100)
      print(final_income)
      
tax_rate=0
income=int(input("Enter your income: "))
question=input("Do you have a tax rate? ")
if(question=="No" or question =="no" or question=="N" or question=="n"):
        if(income<=1000000):
            tax_rate==0
        elif(income>100000 and income<=500000):
            tax_rate==5
        elif(income>500000):
            tax_rate=10
elif(question=="Yes" or question=="yes" or question=="Y" or question=="y"):
        tax_rate=int(input("Enter the tax rate: "))
calculate_tax(income, tax_rate)