#Replacing all  vowels occuring  in a inputted string with asterisks '*'
VOWELS = ['a','e','i','o','u']
string = input("Enter String :")
new_str = ''
for char in string:
    if char.lower() in VOWELS:
        new_str += '*'
    else:
        new_str += char
print("New String is :",new_str)