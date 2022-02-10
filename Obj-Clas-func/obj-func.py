from builtins import print
from classfile import Student

student1 = Student("Ramu", 1, 6.6)
student2 = Student("Kalu", 2, 7.1)
student3 = Student("Samu", 3, 9.3)
student4 = Student("Babu", 4, 7.5)

print(student1.distinction())
print(student2.distinction())
print(student3.distinction())
print(student4.distinction())
