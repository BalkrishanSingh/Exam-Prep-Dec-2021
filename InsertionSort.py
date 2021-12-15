#Sorting a list using insertion sort
items =  eval(input("Enter a list : "))
for index  in range(len(items)):
    while index > 0:
        if items[index-1] > items[index]:
            items[index-1],items[index] = items[index],items[index-1]
        else:
            break
        index -= 1
print("List after sorting",items)