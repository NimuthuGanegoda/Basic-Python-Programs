#Name: Nimuthu Ganegoda
#Student ID: 10695889

#test result check

result = int(input("Enter your result: "))
if result >= 50:
    print("You passed!")
else:
    print("You failed!")

is_passed = input("Did you pass the exam? : ").lower()

if is_passed == "y":
    if result >= 80:
        grade = "HD (High Distinction)"
    elif result >= 70:
        grade = "D (Distinction)"
    elif result >= 60:
        grade = "C (Credit)"
    elif result >= 50:
        grade = "P (Pass)"
    else:
        grade = "F (Fail)"
    print("Congratulations! You passed the exam.")
else:
    grade = "F (Fail)"

print("Your grade is:", grade)