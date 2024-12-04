pet = input("Enter the name of the pet (dog/cat): ").lower()  # Convert input to lowercase
age = int(input("Enter the age of the pet: "))

if age < 0:
    print("Age cannot be negative.")
else:
    if pet == "dog":
        if age < 2:
            print("Your pet needs Puppy Food")
        elif age < 7:
            print("Your pet needs Adult Dog Food")
        else:
            print("Your pet needs Senior Dog Food")
    elif pet == "cat":
        if age < 2:
            print("Your pet needs Kitten Food")
        elif age < 7:
            print("Your pet needs Adult Cat Food")
        else:
            print("Your pet needs Senior Cat Food")
    else:
        print("Invalid pet species. Please enter 'dog' or 'cat'.")