#class task 1
name = "Excel"
age = 18
gpa = 5.0

print("my name is",name,"age is ",age ,"my CGPA IS ", gpa)
print(type(name))
print(type(age))
print(type(gpa))

#class task 2
#1
food = ["fried yam","jellof rice ","fish","beef"]
food[2] = "turkey"
for i in food:
    print(i)

#2
car = {"key": "keyless",
       "model": "F150",
       "brand": "ford"}
print(car["model"])

#3

my_set = {1,1,2,2,2,3,4,2,5}
print(my_set)

#4
color = ("red","blue","green")
print(color[2])


#class task 3
#1
print("task 3")

print("list of even numbers")
for i in range(0,21,2):
    print(i)
#2
print("while loop no 2")
count = 10
while count >=1:
    print(count)
    count -= 1
#3
print("calculate sum from 1 to 100")
sum = 0
for i in range(1,100):
    sum += i
print(sum)


#class task 4 functions
#1
def product(a,b):
    answer = a * b
    print(answer)

product(5,6)

#2
def evenOdd(number):
    if number % 2 == 0:
        print(f"number {number} is even")
    else:
        print("not even")
evenOdd(4)

#3
def factorial(num):
    fac = 1
    for i in range(1,num):
        fac *= i
    print(fac)

factorial(6)