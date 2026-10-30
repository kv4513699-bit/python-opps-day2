# Declaration and calling of instance variable

class Student:
    def __init__(self, name, email, age):
        self.n = name  # declare inside constructor
        self.e = email
        self.a = age
        print(self.n, self.a, self.e)  # calling inside constructor

    def show(self, city):
        self.c = city  # declare inside instance method
        print(self.n, self.e, self.a, self.c, self.roll)

obj = Student("Neeraj", "n@gmail.com", 38)
print(obj.n, obj.a, obj.e)  # calling outside class

obj.roll = 101  # declare outside class with object
obj.show("Bhopal")  # Output: Neeraj n@gmail.com 38 Bhopal 101