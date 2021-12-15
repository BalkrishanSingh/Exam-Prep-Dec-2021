#Check if a number is divisible by another number
dividend = int(input("Enter the Dividend :"))
divisor = int(input("Enter The Divisor :"))
if dividend % divisor == 0:
    print(f"{dividend} is divisible by {divisor}")
else:
    print(f"{dividend} is not divisible by {divisor}")