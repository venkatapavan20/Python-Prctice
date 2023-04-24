'''Create a Student class and initialize it with name and roll number. Make methods to :
1. Display - It should display all informations of the student.
2. setAge - It should assign age to student
3. setMarks - It should assign marks to the student.'''
class Student():
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
newstudent=Student(name="pavan",rollno=666)
class Display(Student):
    def __init__(self,father,height,group):
        self.father=father
        self.height=height
        self.gropu=group
newDisplay=Display(father="venu",height="5.5ft",group="python")
class Setage(Student):
    def __init__(self,age):
        self.age=age
newSetage=Setage(age=22)
class Setmarks(Student):
    def __init__(self,marks):
        self.marks=marks
newSetmarks=Setmarks(marks=555)
 
print("name of the:",newstudent.name)
print("roll no.of student:",newstudent.rollno)
print("father nameof the student:",newDisplay.father)
print("age of the student:",newSetage.age)
print("marks of the students:",newSetmarks.marks)

