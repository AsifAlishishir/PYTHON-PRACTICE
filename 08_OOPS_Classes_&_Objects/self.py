class Employee:
    language='python'
    salary=212200

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

harry=Employee()
# harry.language="JavaScript"
# harry.getInfo()
Employee.getInfo(harry)
harry.greet()