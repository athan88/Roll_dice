from random import randint
#
# classes
#


#
# Die base, contains only one method, roll
#


class Die:

    def __init__(self, sides, value):
        self.sides = sides
        self.value = value

    def roll(self):
        self.value = randint(1, self.sides + 1)

