# Name: Kristine Mae Peralta
# Section: IV-BSIT C
# Activity: P4 - Safe Menu
# Date: November 21, 2026

# Function to divide two numbers
def divide_numbers():
    try:
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))

        result = first / second

    except ValueError:
        print("\nError: Please enter valid numbers.")

    except ZeroDivisionError:
        print("\nError: Cannot divide by zero.")

    else:
        print(f"\nResult: {result:.2f}")

    finally:
        print("\nDivision operation finished.")


# Function to open and read a file
def open_file():
    filename = input("Enter file name: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

    except FileNotFoundError:
        print("\nError: File does not exist.")

    except PermissionError:
        print("\nError: You do not have permission to read this file.")

    else:
        print("\n      FILE CONTENT      ")
        print(content)

    finally:
        print("\nFile operation finished.")


# Main menu
def main():
    while True:
        print("\n      SAFE MENU PROGRAM       ")
        print("1. Divide Two Numbers")
        print("2. Open and Read a File")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            divide_numbers()

        elif choice == "2":
            open_file()

        elif choice == "3":
            print("\nThank you for using the program!")
            break

        else:
            print("\nInvalid menu choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()