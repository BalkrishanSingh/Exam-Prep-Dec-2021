#Count the number of Occurrence of Given Character in a given string
string = input("Enter the String :")
character = input("Enter the Character :")
counter = 0
for i in string:
    if character == i:
        counter += 1
print('Number of Occurrence of Given Character is : ',counter)