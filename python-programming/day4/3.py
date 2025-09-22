<<<<<<< HEAD
'''An abstract method area() (no implementation).
Create two child classes that inherit from Shape:
Rectangle → has attributes length, breadth, and implements area().
Circle → has attribute radius, and implements area().
Task:
Define the abstract class Shape using the abc module.
Implement Rectangle and Circle classes by providing their own version of area().
Create one object of Rectangle and one of Circle, then display their areas.
 '''
class shape:
    def area(self):
        pass
class rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        ar=self.length*self.breadth
        print(f"Area of rectangle : {ar}")
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        pi=3.14
        ar=pi*self.radius**2
        print(f"Area of circle : {ar}")

recobj=rectangle(10,20)
circobj=circle(2)
recobj.area()
circobj.area()
        

=======
'''An abstract method area() (no implementation).
Create two child classes that inherit from Shape:
Rectangle → has attributes length, breadth, and implements area().
Circle → has attribute radius, and implements area().
Task:
Define the abstract class Shape using the abc module.
Implement Rectangle and Circle classes by providing their own version of area().
Create one object of Rectangle and one of Circle, then display their areas.
 '''
class shape:
    def area(self):
        pass
class rectangle(shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        ar=self.length*self.breadth
        print(f"Area of rectangle : {ar}")
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        pi=3.14
        ar=pi*self.radius**2
        print(f"Area of circle : {ar}")

recobj=rectangle(10,20)
circobj=circle(2)
recobj.area()
circobj.area()
        

>>>>>>> d283d138443d18f417b8952a56da15ce85d46d2b
        