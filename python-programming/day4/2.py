<<<<<<< HEAD
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Employee details :")
        print(f"Name : {self.name}\tSalary : {self.salary}")

class manager(employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department
        
    def display(self):
        print("Manager details :")
        print(f"Name : {self.name}\tSalary : {self.salary}\tDepartment : {self.department}")

obje=employee("sindhu",100000)
objm=manager("poojitha",200000,"data analytics")
obje.display()
print()
objm.display()
        
        
=======
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Employee details :")
        print(f"Name : {self.name}\tSalary : {self.salary}")

class manager(employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department
        
    def display(self):
        print("Manager details :")
        print(f"Name : {self.name}\tSalary : {self.salary}\tDepartment : {self.department}")

obje=employee("sindhu",100000)
objm=manager("poojitha",200000,"data analytics")
obje.display()
print()
objm.display()
        
        
>>>>>>> d283d138443d18f417b8952a56da15ce85d46d2b
