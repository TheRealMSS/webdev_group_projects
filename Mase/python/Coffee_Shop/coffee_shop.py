drink = {
    "espresso": 2.50,
    "americano": 3.00,
    "latte": 2.50,
    "cappuccino": 3.00,
    "macchiato": 2.50,
    "mocha": 3.50,
    "flat white": 2.50
    }

size = {
    "medium": 0,
    "large": 1.00,
    "xl": 1.50
}

option = {
    "eat in": 0,
    "take away": 1.00
    }

menu = {
    "drink": drink,
    "size": size,
    "option": option
    }

print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+         The Coffee Shop       +")
print("+              Welcome          +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees:")
print(" > Espresso")
print(" > Americano")
print(" > Latte")
print(" > Cappuccino")
print(" > Macchiato")
print(" > Mocha")
print(" > Flat White")
print("----------------------------")
print("Please pick a drink to order: ")

select_drink = (input("What type of coffee would you like? ")).lower()
print()
print()
print("Please order a size... ")
print("Medium: No Extra, Large: £1.00 or XL: £1.50?: ")
select_size = (input("What size? ")).lower()
print()
print()
select_option = (input("Would like to eat in or take away? ")).lower()

if select_drink in menu['drink'] and select_size in menu['size'] and select_option in menu['option']:
    print("Thank you...")
    print(f"You ordered a/an {select_drink}, size {select_size}, and to {select_option}... ")
    print("Calculating prices.... ")
else:
    print("Invalid option...")
    print("Exiting")
    exit()
        
drink_price = menu['drink'][select_drink]
size_price = menu['size'][select_size]
option_price = menu['option'][select_option]
total_price = drink_price + size_price + option_price

print()
print()
print()
print(f"Total is: £{total_price:.2f}")
print("Thank you for shopping with us! ")
     



    
