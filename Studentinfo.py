class Student:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.subjects = []
        self.marks = {}

    def input_data(self):
        self.name = input("Name: ")
        self.age = int(input("Age: "))

        num_subjects = int(input("Number of subjects: "))
        for _ in range(num_subjects):
            subject = input("Subject Name: ")
            mark = int(input(f"Marks for {subject}: "))
            self.subjects.append(subject)
            self.marks[subject] = mark

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Subjects: {self.subjects}")
        print(f"Marks: {self.marks}")


students = []

n = int(input("Enter number of students: "))
for _ in range(n):
    stu = Student()
    stu.input_data()
    students.append(stu)

# Display all students
for stu in students:
    print("\n---- Student ----")
    stu.display()
