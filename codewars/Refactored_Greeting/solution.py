class Person:
    def __init__(self, name):
        self.name = name

    def greet(self, your_name):
        return f"Hello {your_name}, my name is {self.name}"
