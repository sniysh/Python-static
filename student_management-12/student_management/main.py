from student import StudentModule
from course import CourseModule
from enrollment import EnrollmentModule
from grade import GradeModule
from report import ReportModule

def main():
    student_module = StudentModule()
    course_module = CourseModule()
    enrollment_module = EnrollmentModule()
    grade_module = GradeModule()
    report_module = ReportModule()

    while True:
        print("Student Management System")
        print("1. Add Student")
        print("2. View Student Details")
        print("3. Add Course")
        print("4. View Course Details")
        print("5. Enroll Student in Course")
        print("6. View Student's Courses")
        print("7. Enter Student Grades")
        print("8. View Student Grades")
        print("9. Generate Reports")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_module.add_student()
        elif choice == '2':
            student_module.view_students()
        elif choice == '3':
            course_module.add_course()
        elif choice == '4':
            course_module.view_courses()
        elif choice == '5':
            enrollment_module.enroll_student()
        elif choice == '6':
            enrollment_module.view_enrollments()
        elif choice == '7':
            grade_module.enter_grades()
        elif choice == '8':
            grade_module.view_grades()
        elif choice == '9':
            report_module.generate_reports()
        elif choice == '0':
            print("Exiting the Student Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
