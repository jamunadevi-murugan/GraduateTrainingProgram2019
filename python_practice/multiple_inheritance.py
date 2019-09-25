# class Person:
#     # defining constructor
#     def __init__(self, personAge):
#         self.age = personAge
#
#         # defining class methods
#
#     def showAge(self):
#         print(self.age)
#
#         # end of class definition
#
#
# # defining another class
# class Student:  # Person is the
#     def __init__(self, studentId):
#         self.studentId = studentId
#
#     def getId(self):
#         return self.studentId
#
#
# class Resident(Person, Student):  # extends both Person and Student class
#     def __init__(self, name, age, id):
#         self.name=name
#         Person.__init__(self, age)
#         Student.__init__(self, id)
#
#     def showName(self):
#         print(self.name)
#
#     # Create an object of the subclass
#
#
# resident1 = Resident('John', 30, '102')
# resident1.showName()
# print(resident1.getId())

# class Common:
#     def __init__(self,name):
#         name1=name
#         print(name1)
#
# class A(Common):
#     def __init__(self):
#
#         self.name = 'John'
#         self.age = 23
#         Common.__init__(self.name)
#
#     def getName(self):
#         return self.name
#
#
# class B(Common):
#     def __init__(self):
#         name='jam'
#         self.name = 'Richard'
#         self.id = '32'
#         Common.__init__(self,name)
#
#     def getName(self):
#         return self.name
#
#
# class C(B, A):
#     def __init__(self):
#         super().__init__()
#
#
#     def getName(self):
#         return self.name
#
#
# C1 = C()
# print(C1.getName())

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):
        mark1=self.m1+other.m1
        mark2=self.m2+other.m2
        return Student(mark1,mark2)
    def __gt__(self, other):
        return (self.m1>other.m1 and self.m2>other.m2)
Student1=Student(77,88)
Student2=Student(33,55)
Student3=Student1+Student2
print(Student3.m1,Student3.m2)
print(Student1>Student2)