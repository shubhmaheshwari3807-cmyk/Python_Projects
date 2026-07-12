day_1_list=[]
print("Day 1 visitors: ")
day_1_list.append(input("Enter the name of the person: "))
day_1_list.append(input("Enter the name of the person: "))
day_1_list.append(input("Enter the name of the person: "))

day_1_set=set(day_1_list)

day_2_list=[]
print("Day 2 visitors: ")
day_2_list.append(input("Enter the name of the person: "))
day_2_list.append(input("Enter the name of the person: "))
day_2_list.append(input("Enter the name of the person: "))

day_2_set=set(day_2_list)

print("All the visitors are", day_1_set.union(day_2_set))
print("All those who came on both days are", day_1_set.intersection(day_2_set))
