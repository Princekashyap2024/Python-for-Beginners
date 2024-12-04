# Problem: Calculate the sum of even numbers up to a given number n.

# Prompt the user to enter a number and convert the input to an integer
user_input_number = int(input("Enter the n number: "))

# Initialize a variable to hold the sum of even numbers
sum_even_numbers = 0

# Loop through the range of even numbers from 2 to user_input_number (inclusive)
for even_number in range(2, user_input_number + 1, 2):
    # Add the current even number to the cumulative sum
    sum_even_numbers += even_number

# Print the final sum of even numbers
print("Sum of even number is: ",sum_even_numbers)