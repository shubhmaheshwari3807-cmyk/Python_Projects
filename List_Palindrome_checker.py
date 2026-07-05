#Practice question to check if a list is palindrome or not

list1=[1, 2, 2, 1]
list2=[1, 2, 3, 6]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
    print("It's a palindrome")
else:
    print("It is not a palindrome")

copy_list2=list2.copy()
copy_list2.reverse()

if(copy_list2==list2):
    print("It's a palindrome")
else:
    print("It's not a palindrome")
