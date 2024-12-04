# Problem :- compute the factorial of a number using a while loop.


user_input_factorial = int(input("Enter the number: "))

factorial = 1

while user_input_factorial > 0:
    factorial = factorial * user_input_factorial
    user_input_factorial -= 1

print("The factorial is: " + str(factorial))  # Output: factorial: 720