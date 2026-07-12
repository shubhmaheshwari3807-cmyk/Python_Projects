def generate_username(first_name, last_name, num="1"):
    print(first_name[0:4] + last_name[0:4] + num)

generate_username("ashok", "singh")
generate_username("shiv", "chaudary", "5")

first_name=input("Enter first name: ")
last_name=input("Enter last name: ")
num=int(input("Enter a number: "))
num_str=str(num)

generate_username(first_name, last_name, num_str)
