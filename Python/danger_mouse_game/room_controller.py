import room
import item
# import csv
import character
# from character import Mouse

room_map = {'nest': ['mouse hole'],
            'library': ['mouse hole', 'library door'],
            'east hall': ['library door', 'swinging door', 'servant door', 'master door', 'guest door', "gallery door"],
            'serv chamber': ['servant door', 'servant passage'],
            'gallery': ['gallery door'],
            'guest bedroom': ['guest door'],
            'master bedroom': ['master door'],
            'grand hall': ['swinging door', 'grand arch'],
            'living room': ['grand arch', 'chapel door'],
            'chapel': ['chapel door', 'fsm door'],
            'west hall': ['fsm door', 'kitchen entry'],
            'kitchen': ['kitchen entry', 'serv kitchen', 'buttery entry'],
            'servant hall': ['servant passage', 'serv kitchen'],
            'dresser': ['dresser drawer'],
            'buttery': ['buttery entry'],
            'front lawn': ['front door']
            }



# Room initializations
# name, description, doors[], characters[]
nest = room.Room('nest', "You are in your mouse nest, in a large castle. The belongings in the nest are yours and you recognize all of them. You see your mouse family, hungry and waiting patiently for you to bring home enough food for everyone to eat.", room_map['nest'], [])
library = room.Room('library', 'You are in the library. It once occured to you to read them all, but a mouse like you need not concern itself with such things.', room_map['library'], [])
east_hall = room.Room('east hall', "You are in the east hallway, it's very dark in here. You look around for light leaking under doorways to find your exits.", room_map['east hall'], [])
serv_chamber = room.Room('serv chamber', "The room for the help. They sneak your family cheese sometimes, but they appear busy today.", room_map['serv chamber'], [])
gallery = room.Room('gallery', "You enter the castle art gallery. Its most prized pieces include paintings by Monet, however you've always been more of a Dali fan yourself.", room_map['gallery'], [])
guest_bedroom = room.Room('guest bedroom', "The guest bedroom. You tried to sleep in there once but APPARENTLY don't qualify as a guest.", room_map['guest bedroom'], [])
master_bedroom = room.Room('master bedroom', "The master bedroom. Not a bedroom for the common mouse.", room_map['master bedroom'], [])
grand_hall = room.Room('grand hall', "You enter the grand entry hall. It's pillars and golden statues boast of a life lived in luxury, a red cloth banner on the ceiling reads \"There are no god's or kings, only men.\"", room_map['grand hall'], [])
living_room = room.Room('living room', "You enter the livingroom. Mostly just for show and guests, otherwise the room is rarely used.", room_map['living room'], [])
chapel = room.Room('chapel', "You enter the Chapel room. However Dave doesn't appear to be here at the moment 'man'.", room_map['chapel'], [])
west_hall = room.Room('west hall', "This is the western hallway. The windows allow the sun to illuminate the hall with its shining brilliance, much better hallway than that other one.", room_map['west hall'], [])
kitchen = room.Room('kitchen', "Kitchen, there must be cheese somewhere.", room_map['kitchen'], [])
servant_hall = room.Room('servant hall', "The servants hall. You can't just have your servants walking around the castle like they own the place, right?", room_map['servant hall'], [])
dresser = room.Room('dresser', "You find yourself in a dresser, and much to your own surprise it's filled with clothes! You make a note to come back during winter.", room_map['dresser'], [])
buttery = room.Room('buttery', "The buttery, there's wine and cheese everywhere!", room_map['buttery'], [])
outside = room.Room('front lawn', "You are on the front lawn. You peer upward towards the sky, into the void of infinity. It's a great big universe and you're just a small part of it. The sheer impact of this realization, of having grasped the nature of the cosmos and the universe has unfortunately so blown your mind that it has left you comatose, your family will surely perish. Game Over.",room_map['front lawn'],[])

# Door initializations
# name, description, room1, room2, is_locked, key_name
mouse_hole = room.Door('mouse hole', 'A hole in the baseboard of the castle library, the entry way to your humble home.', nest, library, False, 'mouse hole key')
library_door = room.Door('library door', 'A crack under the door', library, east_hall, False, 'library door key')
swinging_door = room.Door('swinging door', 'A swinging door', east_hall, grand_hall, False, 'swinging door key')
servant_door = room.Door('servant door', 'A wooden door', east_hall, serv_chamber, True, 'servant door key')
gallery_door = room.Door('gallery door', 'It looks like you can squeze through the door', east_hall, gallery, False, 'gallery door key')
guest_door = room.Door('guest door', 'A wooden door', east_hall, guest_bedroom, False, 'guest door key')
master_door = room.Door('master door', 'A wooden door', east_hall, master_bedroom, False, 'master door key')
grand_arch = room.Door('grand arch', 'A large archway', grand_hall, living_room, False, 'grand arch key')
chapel_door = room.Door('chapel door', 'A thick door', living_room, chapel, False, 'chapel door key')
fsm_door = room.Door('fsm door', 'The flying speghetti monster rests on the door', chapel, west_hall, False, 'fsm door key')
kitchen_entry = room.Door('kitchen entry', 'A swinging double door', west_hall, kitchen, False, 'kitchen door key')
buttery_entry = room.Door('butter entry', 'One more door', kitchen, buttery, True, 'buttery door key')
serv_kitchen = room.Door('serv kitchen', 'Servants kitchen entrance', kitchen, servant_hall, False, 'serv door key')
servant_passage = room.Door('servant passage', 'Secret door', serv_chamber, servant_hall, True, 'servant passage key')
dresser_drawer = room.Door('dresser drawer', 'A dresser drawer', master_bedroom, dresser, False, 'dresser drawer key')
front_door = room.Door('front door', 'The front entrance to the castle, really quite a beautiful doorway, not that the opinion of a mouse matters.',grand_hall, outside, False, 'front door key' )


door_dict ={'mouse hole': mouse_hole,
            'library door': library_door,
            'swinging door': swinging_door,
            'servant door': servant_door,
            'gallery door': gallery_door,
            'guest door': guest_door,
            'master door': master_door,
            'grand arch': grand_arch,
            'chapel door': chapel_door,
            'fsm door': fsm_door,
            'kitchen entry': kitchen_entry,
            'buttery entry': buttery_entry,
            'serv kitchen': serv_kitchen,
            'servant passage': servant_passage,
            'dresser drawer': dresser_drawer,
            'front door': front_door
            }

room_dict ={'nest': nest,
            'library': library,
            'east hall': east_hall,
            'serv chamber': serv_chamber,
            'gallery': gallery,
            'guest bedroom': guest_bedroom,
            'master bedroom': master_bedroom,
            'grand hall': grand_hall,
            'living room': living_room,
            'chapel': chapel,
            'west hall': west_hall,
            'kitchen': kitchen,
            'servant hall': servant_hall,
            'dresser': dresser,
            'buttery': buttery,
            'outside': outside
            }

buttery.add_item(item.Food('round'))
buttery.add_item(item.Food('slice'))
buttery.add_item(item.Food('slice'))
chapel.add_item(item.Food('piece'))
kitchen.add_item(item.Food('loaf'))
master_bedroom.add_item(item.Food('slice'))
guest_bedroom.add_item(item.Food('crumb'))
gallery.add_item(item.Food('wedge'))

characters = []
characters.append(character.Person("serv chamber"))
characters.append(character.Dog("servant hall"))
characters.append(character.Cat("master bedroom"))
characters.append(character.Rat("buttery"))


class Level:
    pass


level = Level()

level.room_dict = room_dict
level.door_dict = door_dict

# when passed a list of all the characters and rooms, will sort through them
# and update the locations on each accordingly
def update_all():
    for c in characters:
        if c.location != "Rat Heaven":
            c.activate(level)
    for loc in room_dict.values():
        temp_list = []
        # Strip spells out
        for person in characters:
            if person.location == loc.name:
                temp_list.append(person)
        loc.update_characters(temp_list)
    for c in characters:
        print(c.name, ":", c.location)
# characters = []
# characters.append(character.Person("serv_chamber"))
# characters.append(character.Dog("gallery"))
# characters.append(character.Mouse("Martin", "of Redwall", "gallery"))
#
# while input("(C)ontinue? ").upper() == "C":
#     update_all(characters, room_dict.values())
#     for c in characters:
#         print(c.name, ":", c.location)


# game_over = False
# current_room = nest
# characters = []
# player = Mouse('Mouse', 'Looks like a mouse', current_room)
# while not game_over:
#     failed_door_open = ''
#     current_room.surroundings()
#     user_input = (input('What is  your command?'))
#     user_input = user_input.lower()
#
#
#     if 'open' in user_input:
#         for door in current_room.doors:
#             if door in user_input:
#                 current_room = current_room.open_door(door_dict[door])
#                 break
#
#     if 'use' in user_input:
#         for thing in user_input:
#             if 'key' in thing:
#                 for door in current_room.doors:
#                     if door.name in user_input:
#                         current_room.use_key(door, player)



    # if first == 'open':
    #     current_room = current_room.open_door(door_dict[second])
    # if first == 'look':
    #     if second == 'room':
    #         current_room.look()
    #     if second in current_room.doors:
    #         print("it is a door")
    #     if second in current_room.characters:
    #         print('this is a character')
    # if first == 'peek':
    #     current_room.peek_room(door_dict[second])
