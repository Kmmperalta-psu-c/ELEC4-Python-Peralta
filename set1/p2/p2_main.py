# Name: Kristine Mae Peralta
# Section: IV-BSIT C
# Activity: P2 - Custom Module (Main Program)
# Date: November 19, 2026

# First import style: import module
import student_utils

# Second import style: from module import name
from student_utils import check_status

# Built-in module for date and time
from datetime import datetime


def main():
    grades = []

    print("      STUDENT GRADE REPORT      ")

    while True:
        try:
            count = int(input("How many grades will you enter? "))

            if count > 0:
                break
            else:
                print("Please enter at least one grade.")

        except ValueError:
            print("Invalid input. Enter a whole number.")

    for i in range(count):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    # Use functions from the custom module
    average = student_utils.calculate_average(grades)
    highest = student_utils.get_highest(grades)
    lowest = student_utils.get_lowest(grades)
    status = check_status(grades)

    # Get the current date and time
    report_date = datetime.now()

    print("\n      GRADE REPORT      ")
    print("Grades:", ", ".join(f"{grade:g}" for grade in grades))
    print(f"Average Grade: {average:.2f}")
    print(f"Highest Grade: {highest:g}")
    print(f"Lowest Grade: {lowest:g}")
    print(f"Status: {status}")
    print("\nReport Generated:",
          report_date.strftime("%B %d, %Y - %I:%M %p"))


if __name__ == "__main__":
    main()