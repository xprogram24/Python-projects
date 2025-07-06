with open("exapmple.txt", "w") as file:
    file.write("This is an example file.\n")
    file.write("It contains some sample text.\n")

with open("exapmple.txt","r") as file:
    content = file.read()
    print(content)

with open("exapmple.txt", "a") as file:
    file.write("this is the new  appenden text.\n")

with open("exapmple.txt", "r") as file:
    for line in file:
        print(line.strip())

students = ["Alice", "Bob", "Charlie"]

with open("student.txt","w") as file:
    for student in students:
        file.write(student + "\n")

with open("student.txt", "r") as file:
    for line in file:
        print(line)


#using file on an oop 

class Student:
    def __init__(self,name, score):
        self.name = name
        self.score = score

    def save_to_file(self):
        with open("oopFile.txt","a") as file:
            file.write(f"name : {self.name}  score is {self.score}\n")
        
s1 = Student("mike",80)
s1.save_to_file()

s2 = Student("Excel",90)
s2.save_to_file()

s3 = Student("John",70)
s3.save_to_file()

s4 = Student("TAM",60)
s4.save_to_file()