# Problem :- keep asking user for input until user enter a number between 1 and 10.

user_num = int(input("Enter the number between 1 and 10: "))

while user_num < 1 or user_num > 10:
    user_num = int(input("Invalid input. Please enter a number between 1 and 10: "))
else:
    print("Thank you for entering a valid number")