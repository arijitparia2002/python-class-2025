# Task 5

def get_student_name():
    """Get and validate student name"""
    while True:
        name = input("Enter student name: ").strip()
        try:
            if len(name) == 0:
                raise ValueError("Name cannot be empty.")
            return name
        except ValueError as e:
            print(f"Error: {e}")

# get how many subject the sudent has
def get_number_of_subjects():
    """Get and validate number of subjects"""
    while True:
        try:
            num = int(input("Enter number of subjects (1-10): "))
            if num < 1 or num > 10:
                raise ValueError("Number of subjects must be between 1 and 10.")
            return num
        except ValueError as e:
            if "invalid literal" in str(e):
                print("Error: Please enter a valid number.")
            else:
                print(f"Error: {e}")


# Get the marks from user

def get_scores(num_subjects):
    """Get and validate all scores"""
    scores = []
    for i in range(num_subjects):
        while True:
            try:
                score = int(input(f"Enter score for subject {i+1} (0-100): "))
                if score < 0 or score > 100:
                    raise ValueError("Score must be between 0 and 100.")
                scores.append(score)
                break
            except ValueError as e:
                if "invalid literal" in str(e):
                    print("Error: Please enter a valid number.")
                else:
                    print(f"Error: {e}")
    return scores


def calculate_grade(average):
    """Convert average to letter grade"""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B+"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"


# Let's connect all of them together

def main():
    print("=== Student Grade Manager ===\n")

    try:
        # Get student information
        name = get_student_name()
        num_subjects = get_number_of_subjects()

        print()  # Blank line

        # Get scores -- returning a list that i am storing here <---
        scores = get_scores(num_subjects)

        # Calculate average
        average = sum(scores) / len(scores)
        grade = calculate_grade(average) # Takes the average and returns Grade

    except Exception as e:
        print(f"\nUnexpected error: {e}")


    else:
        # This runs only if no exceptions occurred
        print("\nCalculation successful!")
        print(f"Student: {name}")
        print(f"Scores: {scores}")
        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")
        7

    finally:
        # This ALWAYS runs
        print("\nOperation completed. You have exited the program")
        print("I am finally block, I will be always running at the end")




# call the main function
main()

