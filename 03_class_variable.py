class Student:
    school_name = "SHSS"  # declare inside class body

    def __init__(self, name):
        self.n = name
        Student.school_code = 101  # declare inside constructor
        print(f'line no 81---{school_name}') # calling inside class
        print(f'line no 85---{Student.school_name}')

    def show(self):
        Student.school_city = "Jhingurdha"  # declare inside instance method
        print(f'line no 89---{Student.school_name, Student.school_code, Student.city_pin}')

    @classmethod
    def update_school_code(cls, new_code):
        cls.school_code = new_code  # declare inside class method
        print(f'line no 94---{cls.school_code}')

Student.city_pin = 486889  # declare outside class
obj = Student("Neeraj")
print(f'line no 98---{obj.n}')
obj.update_school_code(999)
obj.roll = 101
obj.show()
print(Student.city_pin, Student.school_name, Student.school_city)