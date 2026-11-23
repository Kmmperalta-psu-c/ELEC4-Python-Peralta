# Name: Kristine Mae Peralta
# Section: IV-BSIT C
# Course: ELEC 4 - Python Programming
# Activity: P2 - Custom Module (student_utils)
# Date: November 19, 2026

# Function to calculate the average grade
def calculate_average(grades):
    return sum(grades) / len(grades)


# Function to determine pass or fail
def check_status(grades):
    average = calculate_average(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


# Function to get the highest grade
def get_highest(grades):
    return max(grades)


# Function to get the lowest grade
def get_lowest(grades):
    return min(grades)