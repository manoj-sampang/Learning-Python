class Student:
    def __init__(self, name, roll, course):
        self.name = name
        self.roll = roll
        self.course = course

    def __str__(self):
        return f"Name: {self.name}, Roll: {self.roll}, Course: {self.course}"


students = []

def add_student():
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")
    students.append(Student(name, roll, course))
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students found!\n")
    for student in students:
        print(student)

def menu():
    while True:
        print("\n1. Add Student\n2. View Students\n3. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

menu()
