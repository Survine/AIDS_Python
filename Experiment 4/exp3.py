score = int(input("Enter your exam score: "))

if 90 <= score <= 100:
    print("Your grade is A")
elif 80 <= score < 90:
    print("Your grade is B")
elif 70 <= score < 80:
    print("Your grade is C")
elif 60 <= score < 70:
    print("Your grade is D")
elif 0 <= score < 60:
    print("Your grade is F")
else:
    print("Invalid score entered")
