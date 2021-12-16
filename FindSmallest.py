#Finding the Smallest value in a list
items = eval(input("Enter a list : "))
min_pos = 0
min = items[min_pos]
for i in range(1,len(items)):
    if min > items[i]:
        min = items[i]
        min_pos = i
print(f"The Smallest Value in list {items} is {min}")
print("The Position of Smallest Value in list is",min_pos)