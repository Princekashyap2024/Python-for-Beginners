# Problem :- Find the first non - repeted character. Give a string, find the first non-repeated character.

# user_input_string = input("Enter the string: ")

user_input_string = "geeksforgeeks"

for char in user_input_string:
    print(char)
    if user_input_string.count(char) == 1:
        print("First non-repeated character is: ", char)
        break
