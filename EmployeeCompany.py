class Employee:
    
    def __init__(self, id, name, salary, raise_in_salary):
        self.id = id
        self.name = name
        self.salary = salary
        self.raise_in_salary = raise_in_salary
    
    def display(self):
        print("Id:",self.id)
        print("Name:",self.name)
        print("Salary:",self.salary)

class Manager(Employee):
    
    def __init__(self, id, name, salary, raise_in_salary, cabin_id):
        Employee.__init__(self, id, name, salary, raise_in_salary)
        self.cabin_id = cabin_id
    
    def display(self):
        Employee.display(self)
        print("Cabin id:",self.cabin_id)

    # def display(self, type):
    #     print(type)


class Developer(Employee):

    def __init__(self, id, name, salary, raise_in_salary, desk_id):
        Employee.__init__(self, id, name, salary, raise_in_salary)
        self.desk_id = desk_id

    def display(self):
        Employee.display(self)
        print("Desk ID:", self.desk_id)



m1 = Manager(1, "ABC", 10000, 1.3, 101)
m1.display()

d1 = Developer(2, "XYZ", 8000, 1.2, 201)
d1.display()
