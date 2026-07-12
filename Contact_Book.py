contact={}
name1=input("Enter name: ")
number1=input("Enter" + " " + name1 + "'s contact number: ")
name2=input("Enter name: ")
number2=input("Enter" + " " + name2 + "'s contact number: ")
name3=input("Enter name: ")
number3=input("Enter" + " " + name3 + "'s contact number: ")

contact[name1]=number1
contact[name2]=number2
contact[name3]=number3

search=input("Which contact do you want to search: ")
if(contact.get(search)==None):
    print("Contact not present")
else:
    print("The contact number of" + " " + search + " " + "is" + " " + contact.get(search)) 

delete=input("Do you want to delete a contact: ")
if(delete=="Yes" or delete=="yes" or delete=="Y" or delete=="y"):
    delete_contact=input("Which contact do you want to delete: ")
    if(contact.get(delete_contact)==None):
        print("Contact not present")
    else:
        del contact[delete_contact]
print("The final contact list is", contact)
