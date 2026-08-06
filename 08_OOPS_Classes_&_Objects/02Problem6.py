import random

class Train:

    def __init__(self, trainNo):
        self.trainNo=trainNo

    def book(self, fro ,to):
        print(f"Ticket is booked in the train no: {self.trainNo} from {fro} to {to}.")

    def status(self):
        print(f"Train no: {self.trainNo} is running on time.")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {random.randint(220, 500)}")

t=Train(122354)
t.book("Dhaka", "Syhllet")
t.status()
t.getFare("Dhaka", "Syhllet")