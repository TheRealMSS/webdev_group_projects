# Coffee Shop Order System

A command-line coffee ordering program that calculates the total price based on drink type, size, and dining option.

## What it does

This program simulates ordering coffee from a shop. It:
- Displays a menu of available drinks
- Asks the user to choose a drink, size, and eat-in/takeaway option
- Validates the user's choices
- Calculates the total price
- Displays a receipt

## How it works

**Data Structure:**
I used nested dictionaries to organize the menu prices:
- `drink` dictionary stores coffee types and their base prices
- `size` dictionary stores size options and their additional costs
- `option` dictionary stores eat-in/takeaway choices and their costs
- `menu` dictionary combines all of these together

**Price Calculation:**
The program adds up three components:
1. Base drink price (e.g., espresso = £2.50)
2. Size surcharge (e.g., large = +£1.00)
3. Dining option cost (e.g., takeaway = +£1.00)

**Validation:**
The code checks if the user's input matches valid options in the menu dictionaries. If any input is invalid, the program exits with an error message.

## What I learned

- Using dictionaries to store related data
- Nested dictionaries (a dictionary containing other dictionaries)
- String formatting with f-strings
- `.lower()` to handle user input regardless of capitalization
- Input validation with `if/else` statements
- Accessing nested dictionary values with `menu['drink'][select_drink]`. This was big for me.
- Formatting prices to 2 decimal places with `:.2f`

## Example usage
```
What type of coffee would you like? latte
What size? large
Would like to eat in or take away? eat in

You ordered a/an latte, size large, and to eat in...
Total is: £3.50
```

## Possible improvements

- Add a loop so customers can order multiple items
- Show the menu prices directly in the display
- Add error handling for typos (suggest closest match)
- Keep a running total for multiple orders

