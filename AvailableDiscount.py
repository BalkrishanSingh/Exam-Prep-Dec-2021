#Check What discount can you avail on the inputted sale amount.
sale = int(input("Enter The Sale Amount : "))
if sale >= 10000:
    print("10% Discount")
elif sale >= 7500:
    print("7% Discount")
elif sale >= 5000:
    print("5% Discount")
elif sale >= 2500 :
    print("3% Discount")
else:
    print("No Discount")