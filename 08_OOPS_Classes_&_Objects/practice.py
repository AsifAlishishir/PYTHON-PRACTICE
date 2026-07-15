class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    @staticmethod
    def hello():
        print("hello")

    def get_Avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hi", self.name, "Your average mark is:", sum/len(self.marks))

s1=Student('asif ali', [99,99,99])
s1.get_Avg()
s1.name="Jannati"
s1.get_Avg()
s1.hello()