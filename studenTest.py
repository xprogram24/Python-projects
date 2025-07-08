class Student:
    def __init__(self, name, score, course_name):
        self.name = name
        self.score = score
        self.course_name = course_name

    # method to save to file
    def save_to_file(self):
        with open("student.txt", "a") as file:
            file.write(f"student name : {self.name}\n")
            for score, course_name in courses.items():
                file.write(f"  {course_name}: {score}\n")
            

    # method to update score
    def update_score(self, new_score):
        self.score = new_score

# while loop to display menu
while True:
    print ("=====welcome user to E-SMS=====")
    print ("1. Add Student")
    print ("2. Update Student Score")
    print ("3. Display Students")
    print ("4. Exit")

    choice = input("Enter your choice: ")

# dictionary to store courses
    courses = {}

    if choice == "1":
        number_of_courses = int(input("Enter number of courses: "))
        name = input("enter student name   :  ")
        for i in range(number_of_courses):  
            
            course_name = input(f"Enter course name {i+1}: ")
            score = input(f"enter student score for {course_name} : ")
            courses[course_name] = score

        Student_obj = Student(name, score , course_name)
        Student_obj.save_to_file()
        print("printing items in file for test......")
        print(f"{courses}")

    elif choice == '2':
        pass

    elif choice == '3':
        with open("student.txt","r") as file:
            for line in file:
                print(line)

    elif choice == '4':
        print ("thank you for using Excel student managment system E-SMS")
        break





























