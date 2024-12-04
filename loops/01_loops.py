# Problem: Given a list of numbers input by the user, count how many are positive.

# Prompt the user to enter numbers separated by spaces
user_input = input("Enter numbers separated by spaces: ")

# Split the input string into a list of strings and convert them to integers
numbers = list(map(int, user_input.split()))

positive_number_count = 0

# Count the positive numbers
for num in numbers:
    if num > 0:
        positive_number_count += 1

print("Final count of positive numbers is:", positive_number_count)