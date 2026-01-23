'''
The Problem:
You're going shopping and want to know if you have enough money!
Your task: Write a program that:
Has a list of item prices in your cart
Uses a loop to add them all up
Calculates the total with 8% tax
Tells you if you can afford it with your budget

Requirements:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Your program must include:
✅ A loop (for or while - your choice!) to add up all the prices
✅ Calculate 8% sales tax on the total
✅ An if/else statement to check if you can afford it
✅ Print the subtotal, tax, final total, and whether you can buy everything

'''


print(f"\n{'='*10} Welcome to LocalCode Technology Electronics{'='*10}\n")



#task 1::::::::

store_items = [
    ["Computer", 5000],
    ["Studio Microphone", 2000],
    ["12 channel Audio Mixer", 3000],
    ["Studio Stereo Headphone",  1600],
    ["Stereo Headphone Distributor", 700],
    ["Microphone Stand", 1200],
    ["USB Sound Card" , 1000],
    ["USB Hub" , 120],
    ["Audio Cables " , 700],
    ["Studio Active Monitor" , 1500],
    ["Nasco TV 32' ", 1200]
]





# set total project Budget 
total_Budget = 15000








# task 2:::::::: for loop
sub_total = 0
                                                    
for item, value in enumerate(store_items, 1):
    print(f"{item}: {value[0]} => GHC{value[1]}")
    sub_total += value[1]
# print(f"GHC{sub_total}")
print()







# task 3:::::: 8% VAT tax
vat_tax = sub_total * (8/100)
vat_tax_amount = round(vat_tax,1)
# print(f"GHC{vat_tax_amount}")









# task 4::::::: budget comparison

total_amount_after_tax = sub_total + vat_tax_amount


print(f"{"="*20} cash  {"="*20}")
print(f"total Budget allocated for the Equipment \nGHC{total_Budget}")
print()
print(f"This is the total amount of the equipement at the store \nGHC{sub_total}")
print()
print(f"This is the 8% VAT Tax on the SubTotal\nGHC{vat_tax_amount}")
print()
print(f"This is the total amount after 8% tax \nGHC{total_amount_after_tax}")
print()


# print(total_amount_after_tax)

if total_Budget > total_amount_after_tax:
    cash_left = total_Budget - total_amount_after_tax 
    print(f"✅ you can afford the total Equipment \nBecause your budget is more than the total Amount\n Amount left is GHC{cash_left}\nThank you")
else:
    cash_needed = total_amount_after_tax - total_Budget
    
    print (f"❌ Kindly note that you can not afford the equipment you have planned to purchase \nbecause you need an amount of GHC{round(cash_needed,1)} \nThank you")


print(f"\n{'='*10} Thank you for shopping with LocalCode Technology Electronics{'='*10}\n")
print("end of Assignment".capitalize())
