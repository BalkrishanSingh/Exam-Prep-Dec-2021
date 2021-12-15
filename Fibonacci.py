#Fibonacci Series is a series where each number is the sum of the preceding two numbers
n = int(input('Get Fibanacci upto number : '))
numbers = [0,1]
previous = 0
current = 1
for i in range(1,n):
    next_num = previous + current
    numbers.append(next_num)
    previous,current = current,next_num
print(f'Fibonacci Series upto {n} is :',*numbers)