class Dog:
    # intrinsically, all dogs have 4 legs
    # this is a class attribute
    # static variables, never changing
    # _legs is a private var, should not be referenced directly
    _legs = 4
    
    def __init__(self, name, age):
        # instance attributes
        self.name = name
        self.age = age # in years
    
    def bark(self):
        return f'{self.name} says woof!'
    
    @staticmethod # decorator
    def calculate_average_age(dogs):
        total_age = sum(dog.age for dog in dogs)
        average_age = total_age / len(dogs) if dogs else 0
        return round(average_age, 2)
    
    
    def getLegs(self):
        return self._legs