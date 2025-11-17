# #Object Oriented Programming
class Student:
    def __init__(self, name, marks, subject):
        self.name = name
        self.mark = marks
        self.subject = subject

s1 = Student("Zayn", 97, "English")
print(s1.name, s1.mark, s1.subject)

s2 = Student("Maryam", 98, "English")
print(s2.name, s2.mark, s2.subject)

class Clgstud:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self): #Methods
        sum = 0
        for i in self.marks:
            sum += i
        print("Hi", self.name,',', "your avg score is", sum/3)

cs1 = Clgstud("Mark", [89, 94, 91])
cs1.get_avg()