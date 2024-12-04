# Problem :- Check if a password is "Week", "Medium", or "Strong". Criteria: < 6 characters(week), 6 - 10 characters(Medium), > 10 characters(strong).  # noqa: E701

password = input("Enter your password: ")
password_len = len(password)

if password_len > 0 and password_len < 6:
    print("Your password is week!")
elif password_len > 6 and password_len < 10:
    print("Your password is medium!")
elif password_len >= 10:
    print("Your password is strong!")
else:
    print("password is invilid!")