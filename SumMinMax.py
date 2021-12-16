#Finding the sum of the integers between the 0 and inputted number.
number = int(input("Enter anumber : "))
min = 0
max = number
sum = 0
if number < 0 :
	min = number
	max = 0
	while min <= max:
		sum += min
		min += 1
else:
	while min <= max:
		sum += min
		min += 1
print(sum)