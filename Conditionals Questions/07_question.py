# Problem :- Customize a coffee order : "Small", "Medium", or "Large" with an option for "Extra Shot" of expresso.

coffee_size = input("What size of coffee you want: ")
extra_shot = True

if extra_shot:
    coffee = coffee_size + " " + "coffee with an extra shot!"
else:
    coffee = coffee_size + "coffee!"

print("Order: ", coffee)