# Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on wednesday.

costumer_age = int(input("Enter your age for Movies tickets: "))
today_day = input("Enter the today day name: ")
ticket_price = 12 if costumer_age >= 18 else 8

if today_day == "wednesday":
    ticket_price -= 2
    print("After the discount your ticket price is $", ticket_price)
else:
    print("Ticket price for you is $",ticket_price)