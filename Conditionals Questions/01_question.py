user_age = int(input("Enter your Age: "))

if user_age > 0 and user_age < 13:
    print("You are Child")
elif user_age > 13 and user_age < 20:
    print("You are Teenager")
elif user_age > 20 and user_age < 60:
    print("You are Adult")
elif user_age > 60:
    print("You are Senior")
else:
    print("You write worng age")