# Problem :- Print the multiplication table for a given number n up to 10, but skip the fifth iteration.

# user_input_number = int(input("Enter the number n: "))
# # Get the user input number
# for print_multiplication_table in range(1, 11):  # Loop from 1 to 10
#     if print_multiplication_table == 5:          # Check if the iteration is the fifth one
#         continue         # Skip the fifth iteration
#     print(f"{user_input_number} x {print_multiplication_table} = {user_input_number * print_multiplication_table}")  # Print the multiplication result

user_input_num = int(input("Enter the number n: "))

for i in range(1, 11):
    if i == 5:
        continue
    print(user_input_num, 'x', i, '=', user_input_num * i)