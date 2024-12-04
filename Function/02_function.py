# Problem: Create a function that takes two numbers as parameters and returns their sum.

def two_number_sum(num1, num2):
    return num1 + num2

# Get user input for two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Call the function and print the result
result = two_number_sum(num1, num2)
print("The sum is:", result)
