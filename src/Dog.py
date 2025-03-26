class Dog:
    # intrinsically, all dogs have 4 legs
    # this is a class attribute
    # static variables, never changing
    # _legs is a private var, should not be referenced directly
    _legs = 4
    
    def __init__(self, name, age, owner=None):
        # instance attributes
        self.name = name
        self.age = age # in years
        self.owner = owner
    
    def bark(self):
        return f'{self.name} says woof!'
    
    @staticmethod # decorator
    def age_in_dog_years(age):
        return age * 7
    
    def getLegs(self):
        return self._legs
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getOwner(self):
        return self.owner
    