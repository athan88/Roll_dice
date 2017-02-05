# OOP python
from Classes import Die
from Functions import create_dice


#
# Global variables
#

amount_of_dice = 10
dice_sides = 6


#
# Main
#

dice_list = create_dice(amount_of_dice, dice_sides, 1)

for die in dice_list:
    current_die = (dice_list[die])
    current_die.roll()
    print(current_die.value)
