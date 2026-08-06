class Programmer:
    company="Microsoft"

    def __init__(self,name,salary, address):
        self.name=name
        self.salary=salary
        self.address=address

p1=Programmer('asif', 100000, "Dhaka")
p2=Programmer('shara',500000, "Barisal")

print(p1.name, p1.salary, p1.address)
print(p2.name, p2.salary, p2.address)