class GradeModule:
    def __init__(self):
        self.grades = {}
        self.file_name = "grades.txt"
        self.load_data()

    def enter_grades(self):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")
        grade = input("Enter student grade for the course: ")

        key = (student_id, course_id)
        self.grades[key] = grade
        print("Grade entered successfully!")
        self.save_data()

    def view_grades(self):
        if not self.grades:
            print("No grades found.")
            return

        print("Grades:")
        for (student_id, course_id), grade in self.grades.items():
            print(f"Student ID: {student_id}, Course ID: {course_id}, Grade: {grade}")

    def load_data(self):
        try:
            with open(self.file_name, "+r") as file:
                for line in file:
                    student_id, course_id, grade = line.strip().split(",")
                    key = (student_id, course_id)
                    self.grades[key] = grade
        except FileNotFoundError:
            pass

    def save_data(self):
        with open(self.file_name, "+w") as file:
            for (student_id, course_id), grade in self.grades.items():
                file.write(f"{student_id},{course_id},{grade}\n")