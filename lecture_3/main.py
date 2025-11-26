"""Student Grade Analyzer - main module."""


def parse_int(value: int | float | str) -> int | None:
    """Convert input value to int if possible, otherwise return None."""
    try:
        value = int(value)
        return value
    except ValueError:
        print("Invalid input. Please enter a number")
        return None


def get_avg(grades: list) -> float | None:
    """Calculate the average grade for a student."""
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        return None


def add_new_student(students: list) -> dict[str, list[int]]:
    """Add a new student to the system."""
    while True:
        name = input("Enter student name: ").strip()
        # Prevent empty names
        if not name:
            print("Name cannot be empty.")
            continue
        # Check for duplicate student
        if any(s["name"].lower() == name.lower() for s in students):
            print("Student already exists. Try again.")
            continue
        return {"name": name, "grades": []}


def add_grades(students: list) -> None:
    """Add grades to a specific student."""
    # Block action if no students are registered
    if not students:
        print("No students found. Please add a student first.")
        return

    while True:
        name = input("Enter your name: ").strip()
        # Find student by name
        student = next((s for s in students if s["name"].lower() == name.lower()), None)
        if student is None:
            print("Invalid name. Try again.")
            continue
        while True:
            grade = input("Enter a grade (or 'done' to finish): ")
            # Exit grade entry
            if grade == 'done':
                return
            grade = parse_int(grade)
            if grade is None:
                continue
            if grade < 0 or grade > 100:
                print(
                    "Invalid input. Please enter a number between 0 and 100."
                )
                continue
            student["grades"].append(grade)


def show_report(students: list) -> None:
    """Display the maximum, minimum, and overall average grade."""
    over_average = []
    print("--- Student Report ---")
    if not students:
        print("No students found. Please add a student first.")
        return
    for student in students:
        average = get_avg(student["grades"])
        if average is not None:
            display_average = round(average, 1)
            over_average.append(display_average)
        else:
            display_average = "N/A"
        print(f"{student['name']}'s average grade is {display_average}.")
    if not over_average:
        print("No grades available.")
        return
    print(
        f'Max Average: {max(over_average)}\nMin Average: {min(over_average)}\n'
        f'Overall Average: {round(sum(over_average) / len(over_average), 1)}'
    )


def top_performer(students: list) -> None:
    """Find and display the student with the highest average grade."""
    # Select only students with the highest average grade
    top_student = max(
        (s for s in students if s["grades"]),
        key=lambda student: get_avg(student["grades"])
    )
    print(
        f"The student with the highest average is {top_student['name']} "
        f"with a grade of {round(get_avg(top_student['grades']), 1)}"
    )


"""Main loop for Student Grade Analyzer."""
students = []
while True:
    print('--- Student Grade Analyzer ---')
    print('1. Add a new student')
    print('2. Add grades for a student')
    print('3. Generate a full report')
    print('4. Find the top student')
    print('5. Exit program')
    choice = parse_int(input("Enter your choice: "))
    if choice is None:
        continue
    if choice == 1:
        students.append(add_new_student(students))
    elif choice == 2:
        add_grades(students)
    elif choice == 3:
        show_report(students)
        input("Press Enter to return to menu...")
    elif choice == 4:
        top_performer(students)
        input("Press Enter to return to menu...")
    elif choice == 5:
        print("Exiting program.")
        break
    else:
        print("Invalid input. Please enter a valid choice.")
