# Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, yellow - Ripe, Browm - overripe).

fruit_name = input("Enter the fruit name:")
fruit_color = input("Ente the color of the fruit:")

if fruit_name == "Banana":
    if fruit_color == "Green":
        print("The banana is unripe")
    elif fruit_color == "Yellow":
        print("The banana is ripe")
    elif fruit_color == "Brown":
        print("The banana is overripe")
    else:
        print("worng fruit color")
else:
    print("worng fruit")