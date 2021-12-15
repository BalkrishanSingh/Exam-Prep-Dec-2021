#Finding the Largest value in a list
items:list = eval(input("Enter a list : "))
max_pos = 0
max = items[max_pos]
for i in range(1,len(items)):
    if max < items[i]:
        max = items[i]
        max_pos = i
print(f"The Largest Value in the List {items} is {max}")
print("The Position of Largest Value in list is",max_pos)