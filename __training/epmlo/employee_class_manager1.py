#!/usr/bin/python

class Employee:
    'Common base class for all employees'
    # class variable that counts number of employees
    empCount = 0

    def __init__(self, name, salary):
        # object attributes
        self.name = name
        self.salary = salary
        # increase the employee count
        Employee.empCount += 1

    # method that displays the total number of employees
    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    # displays information about an Employee
    def displayEmployee(self):
        print "Name : ", self.name,  ", Salary: ", self.salary

class Manager (Employee):
    'Specialized class for manager employees'
    # class variable that counts number of manager objects
    mCount = 0

    def __init__(self, name, salary, departments):
        # initialize superclass object
        Employee.__init__(self, name, salary)
        # object attributes
        self.departments = departments
        # increase the manager count
        Manager.mCount += 1

    # method that displays the name
    def displayEmployee(self):
        print "Manager name : ", self.name

    # prints the departments a Manager is assigned to
    def displayManager(self):
        print "Manager's departments : ", self.departments

#"This would create first object of Employee class"
emp1 = Employee("Emp1", 2000)
#"This would create second object of Employee class"
emp2 = Employee("Emp2", 5000)

#"This would create the two objects of Manager class"
mng1 = Manager("Mng1", 10000, "marketing")
mng2 = Manager("Mng2", 15000, "legal, financial")

emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

mng1.displayEmployee()
mng2.displayEmployee()
print "Total Employee within Manager %d" % Manager.empCount

