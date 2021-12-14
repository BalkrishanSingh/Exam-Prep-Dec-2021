#A Number which is equal to its reverse is called a Palindromic number.
number = input('Enter Number : ')
reversed_digit = int(number[::-1])
number = int(number)
if number == reversed_digit:
    print('The number is a palindrome')
else:
    print('Number is not a palindrome')
