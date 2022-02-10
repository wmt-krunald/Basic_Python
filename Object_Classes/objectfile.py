from builtins import print
from classfile import Employee

employee1 = Employee("Suresh", 12, "Trainee", 8000)
employee2 = Employee("Muhesh", 11, "Trainee", 7000)
employee3 = Employee("Ramesh", 10, "Trainee", 6000)
employee4 = Employee("Raj", 9, "Trainee", 5000 )

print(employee1.name)
print(employee1.em_id)
print(employee1.quali)
print(employee1.salary)

print(employee2.name)
print(employee3.name)
print(employee4.name)