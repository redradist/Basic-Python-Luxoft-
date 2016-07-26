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

class Manager(Employee):
   mCount = 0

   def __init__(self,name,salary,empl_cout):
      self.name = name
      self.salary = salary
      self.empl_cout = empl_cout
      Employee.empCount += 1
      Manager.mCount += 1      

   def displayEmployee(self):
      print "Name: ", self.name

   def displayManager(self):
      print "No of employees:", self.empl_cout

#"This would create first object of Employee class"
emp1 = Employee("Emp1", 2000)
#"This would create second object of Employee class"
emp2 = Employee("Emp2", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

m1 = Manager("M1",1000,3)
m2 = Manager("M2",2000,10)

m1.displayEmployee()
m2.displayEmployee()
print "Total employee %d" % Manager.empCount
print "Total manager %d" % Manager.mCount
m1.displayManager()
