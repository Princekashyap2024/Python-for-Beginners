# Problem :- Reverse a string using a loop.

user_input_string = input("Enter the string: ")
reversed_string = ""

for char in user_input_string:
    reversed_string = char + reversed_string  # Corrected concatenation

print(reversed_string)  # This will now print the reversed string