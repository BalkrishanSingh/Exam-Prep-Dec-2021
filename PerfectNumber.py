number = int(input('Enter Number To Be Verified : '))
factors = [i for i in range(1,number) if number % i == 0]
if sum(factors) == number:
    print(number,'is a Perfect Number.')
else:
    print(number,'is not a Perfect Number')