first_name=input("Enter your first name: ")
surname=input("Enter your surname: ")

initial_username=first_name[0:3]
final_username=surname[0:3]

username=initial_username+final_username+"123"
print("Your username is",username)
print("It's length is", len(username))