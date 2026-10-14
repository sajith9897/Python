class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)


class PartTime(Person):
    def __init__(self, name, age, working_hours):
        super().__init__(name, age)
        self.working_hours = working_hours

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Working Hours:", self.working_hours)


class Consultant(Employee, PartTime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        self.working_hours = working_hours
        self.project_name = project_name

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)
        print("Working Hours:", self.working_hours)
        print("Project Name:", self.project_name)



p1 = Person("Arun", 25)
e1 = Employee("Rahul", 30, "EMP101")
pt1 = PartTime("Anu", 22, 5.5)
c1 = Consultant("Vishnu", 28, "EMP202", 6.5, "Website Development")


print("Person Details")
p1.show_details()

print("\nEmployee Details")
e1.show_details()

print("\nPart-Time Worker Details")
pt1.show_details()

print("\nConsultant Details")
c1.show_details()