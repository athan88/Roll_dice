from Classes import Die

#
# functions
#


# create_dice returns dictionary of dice, needs the amount of dice


def create_dice(dice_amount, sides, value):
    dice_list = {}
    k = 0

    while k < dice_amount:
        dice_list[k] = Die(sides, value)
        k += 1

    return dice_list


# roll_dice returns the total amount of dice rolled, and if a crit was rolled, needs dictionary of dice







