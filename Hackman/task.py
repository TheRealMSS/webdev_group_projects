# The Problem
# You're going shopping and want to know if you have enough money!
# Your task: Write a program that:
# Has a list of item prices in your cart
# Uses a loop to add them all up
# Calculates the total with 8% tax
# Tells you if you can afford it with your budget
# Requirements
# Your program must include:
# ✅ A loop (for or while - your choice!) to add up all the prices
# ✅ Calculate 8% sales tax on the total
# ✅ An if/else statement to check if you can afford it
# ✅ Print the subtotal, tax, final total, and whether you can buy everything



# task1
items = ("mouse", "keyboard", "monitor", "speakers", "webcam")
prices = [20.99, 35.50,20.00, 15.75,10.20]

# task2
total_budget = 100.00
# formula to calculate subtotal, tax and total

subtotal = sum(prices)

tax = subtotal * 0.08

total = subtotal + tax

print(f"Subtotal: GHC{subtotal:.2f}")
print(f"Tax: GHC{tax:.2f}")
print(f"Total: GHC{total:.2f}")   
if total <= total_budget:
    print("you can afford to purchase everything on your list!")
else:
    print("you cannot afford to purchase everything on your list.")


    # answers
#     Subtotal: GHC102.44
# Tax: GHC8.20
# Total: GHC110.64
# you cannot afford to purchase everything on your list