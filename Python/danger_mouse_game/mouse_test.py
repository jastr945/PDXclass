from room import Room
from character import Mouse
from character import Rat
from item import Food


#kitchen = Room("kitchen", "The kitchen", "kitchen", [])
#should have instantiated a room inventory
mouse = Mouse("Horace", "A wise, old mouse.", 'a herp')
kitchen = Room("kitchen", "The kitchen", "kitchen", [])
# should have instantiated a room inventory
mouse = Mouse("Horace", "A wise, old mouse.", kitchen)
#should have instantiated a character inventory
#cheese = Food("cheese", 20)

# print(kitchen.characters)
# kitchen.characters.append(Rat("a rat", []))
# print(kitchen.characters)
# kitchen.inventory.put_in(cheese)
# print(kitchen.inventory)
cheese = Food("cheese", 20)
#
print(kitchen.characters)
kitchen.characters.append(Rat("a rat", []))
print(kitchen.characters)
#
kitchen.inventory.put_in(cheese)
print(kitchen.inventory)

