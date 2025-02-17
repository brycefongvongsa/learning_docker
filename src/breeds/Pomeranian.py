from Dog import Dog

class Pomeranian(Dog):
    
    def __init__(self, name, age):
        # call the parent constructor to get its attributes and to not override them
        super().__init__(name, age)
        self.breed = 'Pomeranian'
    
    def bark(self):
        return f'{self.name} says yip!'