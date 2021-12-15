#A Number which is equal to its reverse is called a Palindromic number.
number = int(input('Enter Number : '))
temp = number
reversed_num = 0
while temp !=0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10
if number == reversed_num:
    print('The number is a palindrome')
else:
    print('Number is not a palindrome')
