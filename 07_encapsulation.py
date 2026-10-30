# Encapsulation: variables, methods are wrap in single unit
# Access Modifiers

class Student:
    def __init__(self):
        self.x = 10          # Public
        self._x = 10         # Protected
        self.__x = 10        # Private (python me name mangling se kaam karta hai)

    def show(self):          # Public method
        print(self.x)

    def _show(self):         # Protected method
        print(self._x)

    def __show(self):        # Private method
        print(self.__x)

    def access_private(self):
        # private ko class ke andar se hi access kar sakte hai
        print(self.__x)
        self.__show()

obj = Student()
print(obj.x)       # Public - ok
print(obj._x)      # Protected - ok but convention se bahar use nahi karna
# print(obj.__x)   # Error - Private
obj.access_private()  # Private ko is tarah access karo