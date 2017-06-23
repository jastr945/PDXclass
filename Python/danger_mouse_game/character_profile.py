"""
This portion of code begins the game play.
The user gets an introduction to the game
and chooses a major player character.

The code instantiates a Mouse object.
This instantiates an Inventory object
for the Mouse.  And the code then adds
two Spell objects to the Mouse's
inventory.

Because the Spells each Mouse character
starts with differ, the choice changes
the game play.

"""

import character, item
import room
import inventory


def create_character():
    """
    This function will go at the beginning of the game play.
    This function allows a user to choose a major player character from a menu.
    :return:
    """
    """
    :return: 
    """
    run_again = True
    while run_again == True:

        print("""
            Welcome to the game Danger Mouse!
            Your goal will be to avoid danger
            while gathering enough food from
            rooms in the castle to last a day.

            You will find various spells to
            aid you.  Keep an eye on your health,
            as you will need to eat throughout
            the day and also store food to bring
            home.

            Please choose a character to play:

            1. Mortimer - a wise mouse with a
            keen understanding of the rats
            and dogs who occupy the castle.

            2. Sydney - a clever mouse skilled
            at hiding and evasion from the rats,
            cats, dogs, and people who occupy
            the castle.

            3. Aster - a brave mouse quick to
            cause fright in cats and people
            who occupy the castle.

            """)

        try:
            choice = input("Do you choose character 1, 2, or 3?\n:")
            if choice == '1' or choice == '2' or choice == '3':
                run_again = False

        except KeyError:
            continue

    if choice == '1':
        """
            Creates character Mortimer.  
        """
        befriend_1 = item.Spell("befriend")
        befriend_2 = item.Spell("befriend")
        char_list = ['Mortimer', 'You are an elderly mouse who\'s body is worn, but who\'s smile is genuine.',
                     'library', [befriend_1, befriend_2]]

    elif choice == '2':
        """
            Creates character Sydney.
        """
        hide_1 = item.Spell("hide")
        hide_2 = item.Spell("hide")
        char_list = ['Sydney',
                     'You try to look at yourself, but you quickly dodge your own gaze and hide in the shadows.',
                     'nest', [hide_1, hide_2]]

    elif choice == '3':
        """
            Creates character Aster.
        """
        scare_1 = item.Spell("scare")
        scare_2 = item.Spell("scare")
        char_list = ['Aster',
                     'Your physical appearance is not notable, but you act with confidence that leaves others intimidated.',
                     'chapel', [scare_1, scare_2]]

    """
    Uses variable player to instantiate a Mouse character and call the needed list of attributes.
    Returns the Mouse character.  
    """
    player = character.Mouse(char_list[0], char_list[1], char_list[2])
    player.inventory.put_in_quiet(char_list[3][0])
    player.inventory.put_in_quiet(char_list[3][1])
    return player
