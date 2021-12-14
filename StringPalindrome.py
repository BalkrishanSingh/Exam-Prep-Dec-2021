#A String which is the same if we reverse it is called a Palindrome
String = input('Enter String : ')
ReveresedString = String[::-1]
if String == ReveresedString:
    print('The String is a palindrome')
else:
    print('The String is not a palindrome')