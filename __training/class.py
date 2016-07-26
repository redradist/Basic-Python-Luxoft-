class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

#This would create first object of Employee class
emp1 = Employee("Zara", 2000)
#This would create second object of Employee class
emp2 = Employee("Manni", 5000)

print "Display emp1"
emp1.displayEmployee()
print "Display emp2"
emp2.displayEmployee()

print "\n\nDisplay the value of class variable"
print "Total Employee %d" % Employee.empCount

print "\n\nAdd/Modify/Delete class attributes"
emp1.age = 7  # Add an 'age' attribute.
print "After adding age attribute to emp1: ",emp1.age
emp1.age = 8  # Modify 'age' attribute.
print "After modifying age attribute on emp1: ", emp1.age
del emp1.age  # Delete 'age' attribute.


setattr(emp1, 'age', 8)
print "Get status of attribute age, using hasattr: ",hasattr(emp1, 'age')
print "Get value of attribute age, using getattr:", getattr(emp1, 'age')
delattr(emp1, 'age')
print "Get status of attribute age after deletion: ",hasattr(emp1, 'age')


