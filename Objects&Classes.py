class Person:

    def __init__(self):

        self.name = "Ashley"
        self.gender = "Female"
        self.age = 21

    def talk(self):
        print("Hi I'm ", self.name)

    def vote(self):
        if self.age < 18:
            print("Not eligible to vote")
        else:
            print("Eligible to vote")


obj = Person()
Person.talk(obj)
Person.vote(obj)
