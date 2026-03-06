class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def dis(self):
        print("name", self.name)
        print("age", self.age)


class Student(Person):   # Inheriting from Person
    def __init__(self, name, age, roll_no, marks):
        super().__init__(name, age)   # Calls Person constructor
        self.roll_no = roll_no
        self.marks = marks

    def diss(self):
        super().dis()
        print("Roll no:",self.roll_no)
        print("marks", self.marks)
students = []
for i in range(5):
    print("Enter the details for student{i+1}:")
    name = input("Name:")
    age = int(input("Age:"))
    roll_no = input("Roll No:")
    marks = input("Marks:")
    students.append(Student(name,age,roll_no,marks))
                    
print("\nstudent Details:")
for student in students:
    student.diss()