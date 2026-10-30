class Student:
    grad = "10th"

    def __init__(self, name):
        self.n = name

    @classmethod
    def update_grad(cls, new_grad):
        cls.grad = new_grad  # class variable ko modify

    def show(self):
        print(self.n, Student.grad)

    @staticmethod
    def welcome_greet(name):  # independent method, no self/cls
        print(f"welcome {name} to my web page")

    @staticmethod
    def by_greet(name):
        print(f"Thanks {name} to visit my web page")

obj = Student("Python")
obj.show()  # Python 10th
obj.update_grad("11th")
obj.show()  # Python 11th

name = input("Enter your name : ")
obj = Student(name)
obj.welcome_greet(name)
obj.by_greet(name)