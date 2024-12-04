# Assign a letter grade based on a student's score:
# A(90 - 100),
# B(80 - 89),
# C(70 - 79),
# D(60 - 69),
# F(below 60).

student_score = int(input("Enter your Score: "))

if student_score >= 90 and student_score <= 100:
    print("Congratulations, You got grade A")
elif student_score >= 80 and student_score <= 89:
    print("Very Good, You got grade B")
elif student_score >= 70 and student_score <= 79:
    print("Good, You got grade C")
elif student_score >= 60 and student_score <= 69:
    print("NYC, You got grade D")
elif student_score >= 0 and student_score <= 69:
    print("That's Good, Atleast You got grade E")
else:
    print("You write worng marks, write correct marks!")