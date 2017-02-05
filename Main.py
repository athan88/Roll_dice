# OOP python
from Functions import create_dice
from Functions import roll_dice
from tkinter import *

#
# Global variables
#
total = 0

amount_of_dice = 10
dice_sides = 8
perpetual = True

dice_list = create_dice(amount_of_dice, dice_sides, 1)


#
# Main
#




#
# GUI
#

#create correct total


# create the window

root = Tk()
root.title("Dice roller 2000")
root.geometry("600x300")



#
# UI variables
#
total_for_ui = StringVar()


def get_total():
    global total
    global total_for_ui

    total = roll_dice(dice_list, perpetual)[1]
    print(total)
    total_for_ui.set(str(total))


#
# creating the frames
#


top_frame = Frame(root)
top_frame.pack(side=TOP, fill=BOTH, expand=TRUE)

middle_frame = Frame(top_frame)
middle_frame.pack(side=BOTTOM, fill=BOTH, expand=TRUE)

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM, fill=BOTH, expand=TRUE)

bottom_frame_right = Frame(bottom_frame)
bottom_frame_right.pack(side=RIGHT, fill=BOTH, expand=TRUE)

bottom_frame_left = Frame(bottom_frame)
bottom_frame_left.pack(side=LEFT, fill=BOTH, expand=TRUE)


# information to display
button_roll = Button(bottom_frame_right, text="ROLL", fg="white", bg="red", command=get_total)
Label = Label(bottom_frame_left, textvariable=total_for_ui, fg="white", bg="black")

# pack info
button_roll.pack(fill=BOTH, side=RIGHT, expand=TRUE)
Label.pack(side=LEFT, fill=BOTH, expand=True)

# kickoff the event loop
root.mainloop()







