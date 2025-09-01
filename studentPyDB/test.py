import pymysql

mydb = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="09155564452",
    database= "E_SMS"
)

cursor = mydb.cursor()
createDB = "CREATE DATABASE  IF NOT EXISTS E_SMS "
createTable = "CREATE TABLE IF NOT EXISTS student( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL ,course VARCHAR(255) NOT NULL ,score VARCHAR(255) NOT NULL )"
cursor.execute(createDB)
cursor.execute(createTable)
print("created")

class Student:
    def __init__(self, name, score, course_name):
        self.name = name
        self.score = score
        self.course_name = course_name

    def save_to_db(self):
            for course, score in courses.items():
                save = "INSERT INTO student (name, course ,score) VALUES (%s,%s,%s)"
                cursor.execute(save,(self.name,course,score))
            mydb.commit()
            
    def update_score(self, name, course_name, new_score):
        update_Query = "UPDATE student SET score = %s WHERE name = %s and course = %s "
        cursor.execute(update_Query,(new_score,name,course_name))
        mydb.commit()
        print(f"course {course_name} successfully updated to {new_score}")








courses = {}
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

        
        Student_obj = Student(name, score, course_name)
        Student_obj.save_to_db(courses)
        print("Student data saved successfully.")
        print(f"Current courses: {courses}")
        
    #update score section would be implemented
    elif choice == "2":
        
        
        cursor.execute("SELECT * FROM student")
        record = cursor.fetchall()
        if not record:
            print("no courses availble to update")
            
        else:
            print("Courses available for update:")
            for row in record:
                print(row)

            name = input("Enter student name: ")
            course_name = input("Enter the course you want to update: ")
            new_score = input("Enter the new score: ")
            Student_obj = Student(name, course_name,new_score)
            Student_obj.update_score(name, course_name, new_score)


    #to display stsudent in db
    elif choice == '3':
        
            displayStudent = "SELECT * FROM student"
            cursor.execute(displayStudent)

            studentData = cursor.fetchall()
            if studentData:
                for student in studentData:
                    print(student)
            else:
                print("No student records found.")

    elif choice == '4':
        print("Thank you for using Excel's Student Management System (E-SMS).")
        break

    else:
        print("Invalid choice. Please try again.")