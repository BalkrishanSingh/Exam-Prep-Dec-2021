#Sorting a list using Bubble Sort.
items = eval(input("Enter a list : "))
length = len(items)
for i in range(length-1):
    for j in range(length-i-1):
        if items[j] > items[j+1]:
            items[j],items[j+1] = items[j+1],items[j]
print("Sorted list of items is",items)