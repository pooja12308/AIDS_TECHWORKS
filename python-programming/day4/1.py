<<<<<<< HEAD
'''Create a class student with the following attributes: name,roll_no,marks
Add a method display() that prints all details of the student.
Create atleast two student objects with different details.
call the display() method for each object'''

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Student details:")
        print(f"Name    : {self.name}")
        print(f"Roll No : {self.roll_no}")
        print(f"Marks   : {self.marks}")

obj1 = Student("Pooja", 101, 88)
obj2 = Student("Riya", 102, 92)
obj1.display()
print()
obj2.display()
=======
'''Create a class student with the following attributes: name,roll_no,marks
Add a method display() that prints all details of the student.
Create atleast two student objects with different details.
call the display() method for each object'''

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Student details:")
        print(f"Name    : {self.name}")
        print(f"Roll No : {self.roll_no}")
        print(f"Marks   : {self.marks}")

obj1 = Student("Pooja", 101, 88)
obj2 = Student("Riya", 102, 92)
obj1.display()
print()
obj2.display()
>>>>>>> d283d138443d18f417b8952a56da15ce85d46d2b
