#Factorial is the product of an integer and all the integers below it.
number = int(input('Enter Number To Get The Factorial Of : '))
Factorial = 1 * number
for integer in range(1,number):
    Factorial *= integer
print(Factorial," is the factorial of ",number)
