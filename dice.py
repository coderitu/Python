import random

##ASCII art
DICE_ART = {
     1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
##Dice attributes
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "


## Function to return Dice images instead of numbers
def generate_dice_faces_diagram(dice_values):
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])

    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)

  
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram



## Validate user input
def parse_input(user_input):

    x = {"1","2","3","4","5","6"}
    if user_input.strip() in x:
        return int(user_input)
    else:
        print("Number must be between 1 to 6")
        raise SystemExit(1)


def roll_dice(dice_int):
    roll_results=[]
    for _ in range(dice_int):
        roll=random.randint(1,6)
        roll_results.append(roll)
    return roll_results
    """NOTE: indentation of return as the return is part of the function and not the loop"""


##Get user input
for i in range(6):
    dice_input=input("How many times do you want to roll [1-6]: ")
    dice_int = parse_input(dice_input)


## roll the dice
    roll_results = roll_dice(dice_int)

    dice_face_diagram = generate_dice_faces_diagram(roll_results)


    print(f"\n{dice_face_diagram}")





