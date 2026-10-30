# 1. Single Level
class Parent:
    p_city = "Bhopal"
    def p_home(self):
        print("Home from parent.......")
    def p_car(self):
        print("Car from parent.......")

class Child(Parent):
    pass

obj = Child()
obj.p_home()
obj.p_car()
print(obj.p_city)

# 2. Multi-Level
class GrandParent:
    city = "Indore"
    def home(self):
        print("Home from grand_parent.......")

class Parent(GrandParent):
    city = "Bhopal"
    def home(self):
        print("Home from parent.......")
    def p_property(self):
        super().home()
        print(super().city)

class Child(Parent):
    pass

obj = Child()
obj.home()
print(obj.city)
obj.p_property()

# 3. Multiple Inheritance
class Parent1:
    city = "Indore1"
    def home(self):
        print("Home from parent1.......")

class Parent2:
    city = "Bhopal2"
    def home(self):
        self_obj = Parent1
        print("Home from parent2.......")

class Child(Parent2, Parent1):
    pass

obj = Child()
obj.home()
print(obj.city)

# 4. Method Overriding with super()
class Parent:
    city = "Bhopal"
    def home(self):
        print("Home from parent.......")
    def car(self):
        print("Car from parent.......")

class Child(Parent):
    city = "Indore"
    def home(self):
        print("Home from child.......")
    def car(self):
        print("Car from child.......")
    def p_property(self):
        super().home()
        super().car()
        print(Parent.city)

obj = Child()
obj.home()
obj.car()
print(obj.city)
obj.p_property()