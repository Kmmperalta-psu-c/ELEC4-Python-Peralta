# Name: Kristine Mae Peralta
# Section: IV-BSIT C
# Activity: P3 - Student Record Manager
# Date: November 20, 2026

# List to store student names
students = []

# Set to prevent duplicate names
student_names = set()


# Function to add a student
def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    # Convert to lowercase when checking duplicates
    if name.casefold() in student_names:
        print("\nStudent already exists.")
    else:
        students.append(name)
        student_names.add(name.casefold())
        print("\nStudent added successfully!")


# Function to remove a student
def remove_student():
    name = input("Enter student name to remove: ").strip()

    for student in students:
        if student.casefold() == name.casefold():
            students.remove(student)
            student_names.remove(student.casefold())
            print("\nStudent removed successfully!")
            return

    print("\nStudent not found.")


# Function to search for a student
def search_student():
    keyword = input("Enter name to search: ").strip()

    if not keyword:
        print("Please enter a search keyword.")
        return

    matches = []

    for student in students:
        if keyword.casefold() in student.casefold():
            matches.append(student)

    if matches:
        print("\nSearch Results:")
        for number, student in enumerate(sorted(matches, key=str.casefold), 1):
            print(f"{number}. {student}")
    else:
        print("\nNo matching student found.")


# Function to display all students
def display_students():
    if not students:
        print("\nNo students available.")
        return

    print("\n      STUDENT LIST      ")

    # Sort names alphabetically
    sorted_students = sorted(students, key=str.casefold)

    for number, student in enumerate(sorted_students, 1):
        print(f"{number}. {student}")

    print(f"Total Students: {len(students)}")


# Main menu
def main():
    while True:
        print("\n      STUDENT RECORD MANAGER      ")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("\n Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Thank you for using Student Record Manager!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# List and Set Explanation:
# A list stores student names and allows duplicate values.
# A set stores unique values and is useful for checking duplicates.
# In this program, I used a list to keep and display student names.
# I used a set to prevent adding the same student name more than once.