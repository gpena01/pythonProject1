# Concession stand program
from collections import Counter

# dictionary {key:value}

menu = {"pizza": 3.00,
        "hotdog": 2.50,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print("---------- MENU ----------")
for key, value in menu.items():
    print(f"{key:8}: ${value:.2f}")
print("--------------------------")

while True:
    food = input("Select an item ('q' to quit): ").lower().strip()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print(f"Sorry, we do not carry {food}. Please select an item from our menu.")

print("---------- YOUR ORDER ----------")
for food in cart:
    total += menu.get(food)

    print(food, end="\n")

# for i in cart:
#     item_count = cart.count(i)
#     if cart.count(i) > 1:
#         print(f"{i}({item_count})")
#     else:
#         print(i)

print("---------- YOUR TOTAL ----------")
print(f"Total: ${total:.2f}")
