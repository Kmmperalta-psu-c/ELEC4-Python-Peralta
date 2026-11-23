# Name: Kristine Mae Peralta
# Section: IV-BSIT C
# Activity: P1 - Student Grade Calculator
# Date: November 18, 2026

# Function to enter and validate grades
def enter_grades():
    grades = []

    while True:
        try:
            count = int(input("\n How many grades will you enter? "))
            if count <= 0:
                print("Please enter at least one grade.")
            else:
                break
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

    return grades


# Function to calculate average
def calculate_average(grades):
    return sum(grades) / len(grades)


# Function to get highest grade
def get_highest(grades):
    return max(grades)


# Function to get lowest grade
def get_lowest(grades):
    return min(grades)


# Function to determine pass or fail
def check_status(grades):
    average = calculate_average(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


# Function to display grade results
def display_results(grades):
    if not grades:
        print("\nNo grades entered yet.")
        return

    print("\n   GRADE RESULTS   ")
    print("Grades:", ", ".join(f"{grade:g}" for grade in grades))
    print(f"Average Grade: {calculate_average(grades):.2f}")
    print(f"Highest Grade: {get_highest(grades):g}")
    print(f"Lowest Grade: {get_lowest(grades):g}")
    print(f"Status: {check_status(grades)}")


# Main menu function
def main():
    grades = []

    while True:
        print("\n   STUDENT GRADE CALCULATOR   \n")
        print("1. Enter Student Grades")
        print("2. View Grade Results")
        print("3. Exit")

        choice = input("\n Enter your choice: ")

        if choice == "1":
            grades = enter_grades()
            print("\n Grades saved successfully!")

        elif choice == "2":
            display_results(grades)

        elif choice == "3":
            print("Thank you for using the Student Grade Calculator!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()


# Local and Global Variables Explanation:
# A local variable is created inside a function and can only be used there.
# For example, count is a local variable inside enter_grades().
# A global variable is created outside functions and can be accessed by other functions.
# In this program, grades is kept local and passed between functions.