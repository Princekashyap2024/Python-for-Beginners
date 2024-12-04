# Problem :- Check if a number is prime.

user_number = int(input("Enter a number: "))

if user_number <= 1:
    print(False)
else:
    is_prime = True  # Assume the number is prime until we find a factor
    for i in range(2, user_number):
        if user_number % i == 0:
            is_prime = False  # Found a factor, so it's not prime
            break  # No need to check further
    print("The number you given is prime: ", is_prime)