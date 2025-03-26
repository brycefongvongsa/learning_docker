from Dog import Dog

class Pomeranian(Dog):
    
    def __init__(self, name, age, owner=None):
        # call the parent constructor to get its attributes and to not override them
        super().__init__(name, age, owner)
        self.breed = 'Pomeranian'
    
    def bark(self):
        return f'{self.name} says yip!'