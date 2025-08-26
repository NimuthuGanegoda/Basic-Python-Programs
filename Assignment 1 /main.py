# This program calculates a student's final grade based on their assessment marks.

def get_valid_mark(prompt):
    """Gets a valid mark between 0 and 100 from the user."""
    while True:
        try:
            mark = float(input(prompt))
            if 0 <= mark <= 100:
                return mark
            else:
                print("That mark doesn't look right. It should be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_grade():
    """Main function to calculate and display student grade."""
    print("Welcome to the Student Grade Calculator!")

    while True:
        student_name = input("Enter the student's name: ")
        student_id = input("Enter the student's ID: ")

        assignment1_mark = get_valid_mark("What was the score for Assignment 1 (0-100)? ")
        assignment2_mark = get_valid_mark("And for Assignment 2 (0-100)? ")
        assignment3_mark = get_valid_mark("How about Assignment 3 (0-100)? ")
        final_exam_mark = get_valid_mark("And the final exam score (0-100)? ")

        # Calculate the total weighted mark.
        total_mark = (assignment1_mark * 0.2) + (assignment2_mark * 0.2) + (assignment3_mark * 0.2) + (final_exam_mark * 0.4)

        # Determine the final grade.
        if total_mark >= 80:
            final_grade = "High Distinction"
        elif total_mark >= 70:
            final_grade = "Distinction"
        elif total_mark >= 60:
            final_grade = "Credit"
        elif total_mark >= 50:
            final_grade = "Pass"
        else:
            final_grade = "Fail"

        # Print out the results.
        print("\n--- Grade Report ---")
        print(f"Student: {student_name}")
        print(f"ID: {student_id}")
        print(f"Final Score: {total_mark:.2f}")
        print(f"Grade: {final_grade}")
        print("--------------------\n")

        go_again = input("Calculate for another student? (yes/no): ").lower()
        if go_again != "yes":
            break

    print("Thanks for using the grade calculator. Goodbye!")

if __name__ == "__main__":
    calculate_grade()
