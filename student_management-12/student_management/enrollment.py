class EnrollmentModule:
    def __init__(self):
        self.enrollments = []
        self.file_name = "enrollment.txt"
        self.load_data()

    def enroll_student(self):
        student_id = input("Enter student ID: ")
        course_id = input("Enter course ID: ")

        enrollment_data = {
            'student_id': student_id,
            'course_id': course_id,
        }

        self.enrollments.append(enrollment_data)
        print("Student enrolled in the course successfully!")
        self.save_data()

    def view_enrollments(self):
        if not self.enrollments:
            print("No enrollments found.")
            return

        print("Enrollments:")
        for enrollment in self.enrollments:
            print(f"Student ID: {enrollment['student_id']}, Course ID: {enrollment['course_id']}")

    def load_data(self):
        try:
            with open(self.file_name, "+r") as file:
                for line in file:
                    student_id, course_id = line.strip().split(",")
                    self.enrollments.append({
                        'student_id': student_id,
                        'course_id': course_id,
                    })
        except FileNotFoundError:
            pass

    def save_data(self):
        with open(self.file_name, "+w") as file:
            for enrollment in self.enrollments:
                file.write(f"{enrollment['student_id']},{enrollment['course_id']}\n")