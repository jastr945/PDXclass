# import character
import inventory
"""
This document contains Item classes for the items in our Danger Mouse game.
The parent class Item defines the subclasses Food and Spell.
"""


class Item:
    def __init__(self, name, description, type, attack=2):
        """
        Instantiates new Item.
        """
        self.name = name
        self.description = description
        self.attack = attack
        self.type = type

    def __str__(self):
        """
        Overloads print function.
        """
        return self.name

    def __repr__(self):
        """
        Determines what the representation will be when it's in a list.
        """
        return self.__str__()

    def look(self):
        print('{}: {}'.format(self.name, self.description))

    # Fish will be instantiated from the Item class, rather than being a class.
    def action(self, room, character):
        character.inventory.put_in(room.inventory.poplar(self.name))

    def use_item(self, room_dict):
        return self.name



class Food(Item):
    """
    Instantiates a Food Item.
    """

    def __init__(self, name):
        scores = {"cheese": 20, "bread": 10, "cake": 30, "loaf": 40, "round": 50, "wedge": 20, "crumb": 10, "slice": 5,
                  "piece": 0}
        descriptions = {"Cheese": "cheese", "bread": "bread", "cake": "cake", "loaf": "A loaf of Tillamook Cheddar",
                        "round": "A partially eaten round of oh so ghouda", "wedge": "A wedge of Brie '86", "crumb": "A small crumb of feta",
                        "slice": "A slice of Amercian cheese", "piece": "A piece of government cheese"}

        self.score = scores[name]
        super().__init__(name, descriptions[name], type='food')


    def look(self):
        super().look()
        print("Score: {}".format(self.score))

    def rat_nibbling(self):
        """
        Allows a rat to nibble on food in a room.
        """
        self.score -= 2
        if self.score <= 0:
            del self

    def eat(self, character_who_eats):
        """
        when called on a food item it will decrement the item food value by 5
        takes input character
        """
        if self.score >= 5:
            amount_food = 5
        else:
            amount_food = self.score
        self.score -= amount_food
        character_who_eats.health += amount_food
        if self.score <= 0:
            character_who_eats.inventory.poplar(self.name)

    def use_item(self, character_who_eats, room_dict):
        self.eat(character_who_eats)

# TODO:  The inventory still needs a way to calculate
#        the total store to win the game.


class Spell(Item):
    def __init__(self, name):
        """
        Instantiates a spell item.
        """
        spells = \
            {"befriend": "The befriend spell allows you to befriend rats and dogs that \
             will help defend you from cats.", "hide": "The hide spell allows you to hide\
            from everyone in the room.", "scare": "The scare spell will scare people and cats\
            out of the room."}
        super().__init__(name, spells[name], 'spell')

    def cast(self, character_who_casts, room_dict):
        where_is = room_dict[character_who_casts.location]
        print('You cast {}, so and so is impressed'.format(self.name))
        cast_spell = 'casted_' + character_who_casts.inventory.poplar(self.name).name

        where_is.inventory.put_in_quiet(Item(cast_spell, "", 'casted'))

    def use_item(self, character_who_casts, room_dict):
        self.cast(character_who_casts, room_dict)



class Weapon(Item):
    def __init__(self, name, description, attack=10):
        super().__init__(name, description, 'weapon', attack)
