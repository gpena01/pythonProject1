# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food item to buy ('q' to quit): ").lower()
    if food == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")
for food in foods:
    print(food)

for price in prices:
    total += price

print("------- TOTAL -------")
print(f"Your total is: ${total:.2f}")