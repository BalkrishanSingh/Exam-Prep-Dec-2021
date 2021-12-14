#Fibonacci Series is a series where each number is the sum of the preceding two numbers
n = int(input('Get Fibanacci upto number : '))
numbers = [i for i in range(n+1)]
for i in range(1,n):
    numbers[i+1] = numbers[i-1] + numbers[i]
print(f'Fibonacci Series upto {n} is :',*numbers)