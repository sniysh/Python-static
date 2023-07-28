
class StudentModule:
    def __init__(self):
        self.students = []
        self.file_name = "students.txt"
        self.load_data()

    def add_student(self):
        name = input("Enter student's name: ")
        student_id = input("Enter student's ID: ")
        grade = input("Enter student's grade: ")
        address = input("Enter student's address: ")

        student_data = {
            'name': name,
            'student_id': student_id,
            'grade': grade,
            'address': address,
        }

        self.students.append(student_data)
        print("Student added successfully!")
        self.save_data()

    def view_students(self):
        if not self.students:
            print("No students in the system.")
            return

        print("Students:")
        for student in self.students:
            print(f"Name: {student['name']}, ID: {student['student_id']}, Grade: {student['grade']}, Address: {student['address']}")

    def load_data(self):
        try:
            with open(self.file_name, "+a") as file:
                for line in file:
                    name, student_id, grade, address = line.strip().split(",")
                    self.students.append({
                        'name': name,
                        'student_id': student_id,
                        'grade': grade,
                        'address': address,
                    })
        except FileNotFoundError:
            pass

    def save_data(self):
        with open(self.file_name, "+w") as file:
            for student in self.students:
                file.write(f"{student['name']},{student['student_id']},{student['grade']},{student['address']}\n")