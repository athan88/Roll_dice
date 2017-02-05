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


# roll_dice returns the total amount of dice rolled, and if a crit was rolled
# needs dictionary of dice and if perpetual is possible

def roll_dice(list_of_dice, perpetual):
    result = [False, 0]

    # getting each die
    for die in list_of_dice:
        current_die = (list_of_dice[die])

        # rolling the die
        current_die.roll()
        roll = current_die.value
        result[1] += roll

        # checking for crits, and rolling again
        if perpetual:
            while roll == current_die.sides:
                print(current_die.value)
                current_die.roll()

                result[1] += current_die.value
                result[0] = True

                roll = current_die.value

            print(roll)
        else:
            result[0] = True

    return result



