quantity = int(input("enter the number of packages you want to buy: "))

if quantity > 100:
    discount = 30
elif quantity >= 51 and quantity <= 100:
    discount = 25
elif quantity >= 21 and quantity <= 50:
    discount = 20
elif quantity >= 10 and quantity <= 20:
    discount = 10
else:
    discount = 0

print("You are buying ", quantity, " packages.")
print("The discount percentage is: ", discount, "%")