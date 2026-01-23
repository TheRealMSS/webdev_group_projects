Odonti's Project Folder


# list of items prices found in my cart.
cart_prices = [40.89, 32.78, 34.23, 46.65]

# my budget.
budget = 100

subtotal = 0
for prices in cart_prices:
    subtotal += prices

#  Tax (8%).
tax = subtotal * 0.08

# calculate final total.
total = subtotal + tax

# price cost
print(f"subtotal: ${subtotal: .2f}")
print(f"tax (8%): ${tax: .2f}")
print(f"total: ${total: .2f}")

# check if you can afford.
if total <= budget:
    print("You can afford")
else:
    print("You do not have enough money")
