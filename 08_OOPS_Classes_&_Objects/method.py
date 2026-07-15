class Student:
    # name='asif'
    college='diit'
    def __init__(self, name, marks):
        # print(self)
        self.name=name;
        self.marks=marks
        print('adding new student in database...')

    def hello(self):
        print("welcome student", self.name)

s1=Student('mili',83)
s1.hello()
print(s1.name, s1.marks)

# s2=Student('sadia',88)
# print(s2.name, s2.marks)

# print(Student.name)