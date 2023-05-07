from random import randint

class Die:
    """A class to simulate a dice roll."""
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        print(randint(1, self.sides))


dicehe = Die(20)
dicehe.roll_die()

