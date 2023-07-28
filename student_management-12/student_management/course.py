class CourseModule:
    def __init__(self):
        self.courses = []
        self.file_name = "courses.txt"
        self.load_data()

    def add_course(self):
        course_name = input("Enter course name: ")
        course_id = input("Enter course ID: ")
        duration = input("Enter course duration: ")
        instructor = input("Enter course instructor: ")

        course_data = {
            'name': course_name,
            'course_id': course_id,
            'duration': duration,
            'instructor': instructor,
        }

        self.courses.append(course_data)
        print("Course added successfully!")
        self.save_data()

    def view_courses(self):
        if not self.courses:
            print("No courses in the system.")
            return

        print("Courses:")
        for course in self.courses:
            print(f"Name: {course['name']}, ID: {course['course_id']}, Duration: {course['duration']}, Instructor: {course['instructor']}")

    def load_data(self):
        try:
            with open(self.file_name, "+r") as file:
                for line in file:
                    name, course_id, duration, instructor = line.strip().split(",")
                    self.courses.append({
                        'name': name,
                        'course_id': course_id,
                        'duration': duration,
                        'instructor': instructor,
                    })
        except FileNotFoundError:
            pass

    def save_data(self):
        with open(self.file_name, "+w") as file:
            for course in self.courses:
                file.write(f"{course['name']},{course['course_id']},{course['duration']},{course['instructor']}\n")
