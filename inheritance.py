class Roopan:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print (f"Name: {self.name}")
        print (f"Age: {self.age}")

class Student(Roopan):
    def __init__(self, name, age, Rollno):
       self.name = name
       self.age = age
       self.Rollno = Rollno

    def show(self):
       super().show()
       print(f"Rollno: {self.Rollno}")

s1 = Student("Rupan",20,19)
s1.show()


        