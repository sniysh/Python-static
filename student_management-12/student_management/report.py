from grade import GradeModule
from enrollment import EnrollmentModule

class ReportModule:
    def __init__(self):
        self.grade_module = GradeModule()
        self.enrollment_module = EnrollmentModule()

    def generate_reports(self):
        print("Generating reports...")
        self.generate_enrollment_report()
        self.generate_average_grade_report()

    def generate_enrollment_report(self):
        enrollments = self.enrollment_module.enrollments
        if not enrollments:
            print("No enrollments found.")
            return

        print("Enrollment Report:")
        for enrollment in enrollments:
            student_id = enrollment['student_id']
            course_id = enrollment['course_id']
            student = self.find_student_by_id(student_id)
            course = self.find_course_by_id(course_id)

            if student and course:
                print(f"Student: {student['name']}, Course: {course['name']}")

    def generate_average_grade_report(self):
        grades = self.grade_module.grades
        if not grades:
            print("No grades found.")
            return

        print("Average Grade Report:")
        course_grades = {}
        course_count = {}

        for (student_id, course_id), grade in grades.items():
            course = self.find_course_by_id(course_id)

            if course:
                if course_id in course_grades:
                    course_grades[course_id] += int(grade)
                    course_count[course_id] += 1
                else:
                    course_grades[course_id] = int(grade)
                    course_count[course_id] = 1

        for course_id, total_grades in course_grades.items():
            course = self.find_course_by_id(course_id)
            average_grade = total_grades / course_count[course_id]
            print(f"Course: {course['name']}, Average Grade: {average_grade:.2f}")

    def find_student_by_id(self, student_id):
        return next((student for student in self.enrollment_module.students if student['student_id'] == student_id), None)

    def find_course_by_id(self, course_id):
        return next((course for course in self.enrollment_module.courses if course['course_id'] == course_id), None)
