class Student:
    def __init__(self, name, email, age):
        self.n = name
        self.e = email
        self.a = age
        print(id(self))

obj = Student("Neeraj", "n@gmail.com", 38)
print(id(obj))

# Proof: self aur obj ka id same hota hai
# self = current object ka address

class Demo:
    pass

print(dir(Demo))
obj1 = Demo()
obj2 = Demo()
print(id(obj1), id(obj2)) # dono ka alag id