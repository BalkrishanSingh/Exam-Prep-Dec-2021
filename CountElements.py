#Counting the number Of elements in a list
items = eval(input("Enter The List : "))
count = 0
for _ in items:
    count += 1
print("No of Elements in the list",count)