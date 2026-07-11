inventory={}
item1=input("Enter first item: ")
price_of_item1=int(input("Enter price of the item: "))
quantity_of_item1=int(input("Enter quantity of the items: "))
item_one=(price_of_item1, quantity_of_item1)

item2=input("Enter second item: ")
price_of_item2=int(input("Enter price of the item: "))
quantity_of_item2=int(input("Enter quantity of the items: "))
item_two=(price_of_item2, quantity_of_item2)

inventory[item1]= item_one
inventory[item2]= item_two

print("the current inventory is", inventory)

new_item=input("Which item do you want to update: ")
new_quantity=int(input("Enter the new quantity: "))

old_price=inventory[new_item][0]
inventory[new_item]=(old_price, new_quantity)
print(inventory)
