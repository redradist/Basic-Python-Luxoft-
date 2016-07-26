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

#"This would create first object of Employee class"
emp1 = Employee("Emp1", 2000)
#"This would create second object of Employee class"
emp2 = Employee("Emp2", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount


