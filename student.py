class Student:
    def __init__(self, name, score, course_name):
        self.name = name
        self.score = score
        self.course_name = course_name

    # method to save to file
    def save_to_file(self, courses):
        with open("student.txt", "w") as file:  # 'w' overwrites old data
            file.write(f"student name : {self.name}\n")
            for course, score in courses.items():
                file.write(f"  {course}: {score}\n")

    # method to update score
    def update_score(self, course_name, new_score, courses):
        if course_name in courses:
            courses[course_name] = new_score
            print(f"Course '{course_name}' updated successfully.")
        else:
            print("Course not found.")


# dictionary to store courses
courses = {}
Student_obj = None  # will hold the current student object

# while loop to display menu
while True:
    print("===== Welcome to E-SMS =====")
    print("1. Add Student")
    print("2. Update Student Score")
    print("3. Display Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        number_of_courses = int(input("Enter number of courses: "))
        name = input("Enter student name: ")

        for i in range(number_of_courses):
            course_name = input(f"Enter course name {i+1}: ")
            score = input(f"Enter student score for {course_name}: ")
            courses[course_name] = score

        # Store the last course entered in the object (keeping your class design)
        Student_obj = Student(name, score, course_name)
        Student_obj.save_to_file(courses)
        print("Student data saved successfully.")
        print(f"Current courses: {courses}")

    elif choice == '2':
        if not courses:
            print("No courses available to update.")
            continue

        print("Courses available for update:")
        for course, score in courses.items():
            print(f"{course}: {score}")

        course_name = input("Enter the course you want to update: ")
        new_score = input("Enter the new score: ")
        Student_obj.update_score(course_name, new_score, courses)
        Student_obj.save_to_file(courses)

    elif choice == '3':
        try:
            with open("student.txt", "r") as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("No student records found.")

    elif choice == '4':
        print("Thank you for using Excel's Student Management System (E-SMS).")
        break

    else:
        print("Invalid choice. Please try again.")
