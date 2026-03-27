class User:
    def __init__(self, name="Bob", age=10, hobbies=None):
        self.name = name
        self.age = age
        self.hobbies=hobbies

    def set_hobbies(self, hobbies:str):
        self.hobbies = hobbies.split(',')