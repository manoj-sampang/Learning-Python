"""Write a Python program that:

Asks the user to enter their name.

Asks for their marks in 3 subjects (e.g., Math, Science, English).

Calculates the average of the marks.

Displays the name, total marks, average, and grade using this grading system:"""

def insert(n):
    names = []
    maths = []
    science = []
    english = []

    for i in range(n):
        print(f"\nStudent {i + 1}")
        name = input("Name: ")
        names.append(name)

        maths.append(int(input("Maths: ")))
        science.append(int(input("Science: ")))
        english.append(int(input("English: ")))

    # Display all data
    for i in range(n):
        total = maths[i] + science[i] + english[i]
        avg = total / 3

        if avg >= 90:
            grade = 'A'
        elif avg >= 80:
            grade = 'B'
        elif avg >= 70:
            grade = 'C'
        elif avg >= 60:
            grade = 'D'
        else:
            grade = 'F'

        print(f"\n--- Result for {names[i]} ---")
        print(f"Total: {total}")
        print(f"Average: {avg:.2f}")
        print(f"Grade: {grade}")


# Main program
print("Enter the number of students:")
n = int(input("Number: "))
insert(n)
