import inventory
import item
import character
import room_controller

# a_rat = character.Mouse('a rat', "ratlike in appearance", 'nest', 100)
# a_food = item.Food('cheese')
#
# a_food.eat(a_rat)
#
# print(a_food.score)
#
# a_rat.inventory.put_in(item.Spell('befriend'))
#
# a_rat.inventory.bag_of_holding[0].cast(a_rat)
#
# room_controller.room_dict["nest"].inventory.list_inventory()

a_rat = character.Mouse('a rat', "ratlike in appearance", 'nest', 100)
a_food = item.Food('cheese')

a_rat.inventory.put_in(a_food)
a_rat.inventory.list_inventory()

a_rat.inventory.bag_of_holding[0].use_item(a_rat)
a_rat.inventory.list_inventory()
a_rat.inventory.bag_of_holding[0].use_item(a_rat)
a_rat.inventory.list_inventory()
a_rat.inventory.bag_of_holding[0].use_item(a_rat)
a_rat.inventory.list_inventory()
a_rat.inventory.bag_of_holding[0].use_item(a_rat)
a_rat.inventory.list_inventory()
