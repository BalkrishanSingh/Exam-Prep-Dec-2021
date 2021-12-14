#Armstrong number is a number for which  the sum of its digit raised by the power of its length is equal to it. 
number = int(input('Enter Number To Be Verified : '))
digits = [int(digit) for digit in str(number)]
sum_cubes = 0
for digit in digits:
    sum_cubes += digit**len(digits)
if number == sum_cubes:
    print(number,'is a Armstrong Number')
else:
    print(number,'is not a Armstrong Number')