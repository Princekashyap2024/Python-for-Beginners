# Problem :- suggest an activity based on the weather (e.g., sunny - Go for a walk, Rainy - read a book, Snowy - Build a snowman).

Weather = input("Enter the weather: ")
sunny = "Go for a walk"
rainy = "read a book"
snowy = "Build a snowman"

if Weather == "sunny":
    print(sunny)
elif Weather == "rainy":
    print(rainy)
elif Weather == "snowy":
    print(snowy)
else:
    print("you write worng weather, verify again!")