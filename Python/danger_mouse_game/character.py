"""
This document contains Classes for the Characters in our Danger Mouse game.
"""

from random import randrange
from random import choice
from inventory import Inventory
import item

spell_list = ["scare", "hide", "befriend"]

"""The Character class creates characters for our group game."""


class Character:
    """The Character class creates characters for our group game."""

    def __init__(self, name, description, loc, health=100):
        """
        Initiates a Character object.
        """
        self.location = loc
        self.description = description
        self.name = name
        self.inventory = Inventory(name)
        self.health = health

    def __str__(self):
        """
        Overloads print function.
        """
        return "{}".format(self.name)
        # this puts those values into a string, which you need

    def __repr__(self):
        """
        Determines what the representation will be when it's in a list.
        """
        return "{}".format(self.name)

    def move(self):
        """
        Allows a user to choose to leave / enter rooms.
        """
        pass

    def activate(self, level):
        """Runs the ai of a character so it can move and act"""
        pass

    def look(self):
        print(self.description)

    def die(self):
        print("Oh no! {} has died".format(self.name))

    def action(self, room, player):
        print('You try to do something to {} but nothing happens'.format(self))


class Mouse(Character):
    """
    Instantiates a Mouse or player character.
    """

    def __init__(self, name, description, loc, health=100):
        """Initiates a Mouse object."""
        super().__init__(name, description, loc, health)
        self.inventory = Inventory(name)

    def take_food(self, my_food):
        """
        This function works on food items and allows you to eat them and gain
        health or put them in inventory.
        """

        choice = input("Add to health(h) or inventory(i)?")
        if choice == "h":
            self.health += my_food.score
            return self.health
        elif choice == "i":
            self.inventory.put_in(my_food)
            return self.inventory

    def take_item(self, my_item):
        """
        This function works on any non-food item, whether spell or fish.
        """
        self.inventory.put_in(my_item)

    def cast_spell(self, my_spell):
        """
        Casts spell by placing a casted spell in the room inventory.
        Charters in room will then be affected by casted_spells in
        room inventory.
        """
        my_spell.name = "casted_" + my_spell.name
        # Name is an attribute of object that is a string.
        # Add my_spell to the room inventory,
        # Remove my_spell from the mouse inventory.

    def damage(self, damage, source):
        print("You take {} damage from {}.".format(damage, source))
        self.health -= damage


class Rat(Character):
    """
    Instanties a Rat character.
    """

    def __init__(self, loc, aggression=randrange(0, 2)):
        super().__init__('rat', 'a rat', loc)
        self.aggression = aggression
        self.friend = False

    def activate(self, level):
        """
        Determines how rat interacts with rooms, room inventories
        (casted spells), and mouse in room.
        """

        # Rats nibble on food and move around randomly, if a cat is in the same
        # room, they will eat the rat and ignore the mouse if its there
        # befriending a rat will have it follow you, beneficial in that it will
        # stop nibbling food and will distract a cat for a turn
        #

        room = level.room_dict[self.location]

        if room.check_inventory("casted_befriend") and self.aggression < 3:
            self.friend = True

        if self.friend:
            for key in level.room_dict.keys():
                if level.room_dict[key].get_character_by_type(Mouse):
                    self.location = level.room_dict[key].get_character_by_type(Mouse).location
        else:
            if room.inventory.look_for_type(item.Food) and randrange(self.aggression, 3) == 2:
                room.inventory.look_for_type(item.Food).rat_nibbling()
            else:
                options = room.get_adjacent(level.door_dict)
                if options:
                    self.location = options[randrange(0, len(options))].name


class Cat(Character):
    def __init__(self, loc, aggression=randrange(2, 3)):
        """
        Instantiates a Cat character.
        """
        super().__init__("Cat", "A cat", loc)
        self.aggression = aggression
        self.turns_until_move = randrange(3, 6)
        self.destination = ""

    def activate(self, level):
        """
        Determines how cat interacts with rooms, inventories in rooms (casted
        spells), and mouse in room.
        """

        room = level.room_dict[self.location]

        if not self.destination:
            destinations = level.room_dict.copy()
            destinations.pop(self.location)
            while not self.destination and destinations:
                temp = choice(list(destinations.keys()))
                if room.find_path(temp, level.door_dict):
                    self.destination = temp
                else:
                    destinations.pop(temp)

        if room.check_inventory("casted_scare") and self.aggression < 3:
            self.turns_until_move = 0
        elif room.get_character_by_type(Dog):
            print("Dog chases cat away")
            self.turns_until_move = 0
            if room.get_character_by_type(Dog).friend:
                room.get_character_by_type(Dog).resting = True
        elif room.check_inventory("fish"):
            self.turns_until_move += 3
            room.inventory.poplar("fish")
        elif room.get_character_by_type(Rat):
            room.get_character_by_type(Rat).die()
            room.get_character_by_type(Rat).location = "Rat Heaven"
            room.characters.remove(room.get_character_by_type(Rat))
        elif room.get_character_by_type(Mouse) and not room.inventory.check_inventory('casted_hide'):
            room.get_character_by_type(Mouse).damage(20, "the claws of a cat")
        else:
            self.turns_until_move -= 1

        # if turns_until_move == 1 and self.inventory.check_inventory("bell"):  # And inventory includes bell
        #     # If the destination room is the room with mouse, alert player
        #     pass
        if self.turns_until_move <= 0 and self.destination:
            self.location = self.destination
            self.destination = ""
            self.turns_until_move = randrange(3, 6)

class Dog(Character):
    searching = 0
    resting = False

    def __init__(self, loc, aggression=randrange(1, 4)):
        """
        Instantiates a Dog character.
        """
        super().__init__("dog", "a dog", loc)
        self.aggression = aggression
        self.friend = False
        self.resting = False
        self.searching = 0

    def activate(self, level):
        """
        Determines how Dog character interacts with room, inventory in room
        (casted spells), and mouse in room.
        """
        room = level.room_dict[self.location]

        # The dog naps until alerted to a mouse, then alerts nearby human and
        # randomly searches for 5 turns after the mosue escapes
        # If its a friend, it will chase off a cat once before stopping to rest

        if not self.friend:
            if room.get_character_by_type(Mouse) and not room.check_inventory("casted_hide"):
                if self.searching:
                    room.get_character_by_type(Mouse).damage(30, "The jaws of a dog")
                    for key in level.room_dict.keys():
                        if level.room_dict[key].get_character_by_type(Person):
                            if not level.room_dict[key].get_character_by_type(Person).path:
                                print("BARK")
                                level.room_dict[key].get_character_by_type(Person).path = level.room_dict[key].find_path(room.name, level.door_dict)
                else:
                    print("The dog smells something and begins to search...")
                self.searching = 1 + self.aggression
            elif self.searching:
                self.searching -= 1
                if room.get_adjacent(level.door_dict):
                    self.location = choice(room.get_adjacent(level.door_dict)).name
        elif not self.resting:
            for key in level.room_dict.keys():
                if level.room_dict[key].get_character_by_type(Mouse):
                    self.location =level.room_dict[key].get_character_by_type(Mouse).location

        if room.inventory.check_inventory("casted_befriend") and self.aggression < 2:
            self.friend = True
            self.resting = False

class Person(Character):
    def __init__(self, loc, aggression=randrange(1, 5)):
        """
        Instantiates a Person character.
        """
        super().__init__("person", "a person", loc)
        self.aggression = aggression
        self.seen_mouse = False
        self.path = ""
        self.home_room = loc

    def activate(self, level):
        """
        Determines how Person interacts with rooms, room invenstories
        (casted spells), and mouse in room.
        """
        # Humans mostly stand still and mind their own business but are still
        # dangerous, either attacking hard or calling other characters nearby.
        # once a mouse leaves a room where the human has seen the mouse, a trap
        # will be laid
        # Humans will also be summoned by barking dogs, if not interrupted by
        # seeing the mouse, they will go to where the dog barked and then back
        #
        room = level.room_dict[self.location]
        if room.inventory.check_inventory("casted_scare") and self.aggression < 3:
            # set a random destination
            pass
        elif room.get_character_by_type(Mouse) and not room.check_inventory("casted_hide"):
            if self.aggression <= 2:
                print("SCREAM")
                for key in level.room_dict.keys():
                    if level.room_dict[key].get_character_by_type(Cat):
                        print("SCREAM")
                        level.room_dict[key].get_character_by_type(Cat).destination = location
                        level.room_dict[key].get_character_by_type(Cat).turns_until_move = 0
            else:
                room.get_character_by_type(Mouse).damage(40, "a knife wielding human")
                self.path = ""
                self.seen_mouse = True
        elif self.path:
            self.location = self.path.pop(0)
        else:
            if self.seen_mouse:
                # set trap
                self.seen_mouse = False
            elif self.location != self.home_room:
                self.path = level.room_dict[self.location].find_path(level.room_dict[self.home_room], level.door_dict)
