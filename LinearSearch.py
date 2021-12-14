items = eval(input("Enter a List :"))
print("List of items is :",items)
target = int(input("Enter Item to Search :"))
found = False
for i in range(len(items)):
    if items[i] == target:
        print("Item found at position:",i+1)
        found = True
        break
if not found:
    print("Item not found in given list")
    
    