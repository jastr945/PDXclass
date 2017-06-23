from inventory import Inventory

class Room():
    def __init__(self, name,  description, doors, characters):
        self.name = name
        self.description = description
        self.doors = doors
        self.characters = characters
        self.inventory = Inventory(name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def open_door(self, door): #character.inventory
        if door.is_locked == True:
            pass
        else:
            if self.name == door.front.name:
                return door.back
            if self.name == door.back.name:
                return door.front
        return self

    def add_item(self, item):
        self.inventory.put_in_quiet(item)

    def update_characters(self, characters):
        self.characters = list(characters)

    def remove_item(self, item):
        self.inventory.poplar(item)

    def check_inventory(self, item):
        self.inventory.check_inventory(item)

    def get_character_by_type(self, character_type):
        for c in self.characters:
            if type(c) == character_type:
                return c
        return ""

    def look(self):
        print(self.description)
        for character in self.characters:
            print("{} is in the room".format(character))
        for item in self.inventory.bag_of_holding:
            print("{} is in the room".format(item.description))
        for door in self.doors:
            print("You can exit through {}".format(door))

    def use_key(self, door, player):
        if door.is_locked == True and player.inventory.check_inventory(door.key):
            print('The door is unlocked.')
            door.is_locked = False
        if door.is_locked == False:
            print('The door is already unlocked')

    def peek_room(self, door):
        '''Look around/examine/search room'''
        if self.name == door.front.name:
            print(door.back.name)
            for character in door.back.characters:
                print('characters in room: {}'.format(character))
        if self.name == door.back.name:
            print(door.front.name)
            for character in door.front.characters:
                print('characters in room: {}'.format(character))

    # def look(self):
    #     '''Singular/specific inspection for items, doors, etc'''
    #     print(self.name + '\n' +self.description + '\n')
    #     print('Exits')
    #     for door in self.doors:
    #         print(door)

    def find_path(self, destination, door_dict):
        # generate dict tree
        nav_tree = {}
        checked = [self]
        level = [self]
        next_level = []
        # nav_tree, checked = self.generate_tree_level(nav_tree, self, door_dict, checked)
        # for t in nav_tree[self]:
        #     level.append(t)
        while level:
            for r in level:
                nav_tree, checked = self.generate_tree_level(nav_tree, r, door_dict, checked)
                for t in nav_tree[r]:
                    next_level.append(t)

            level = next_level
            next_level = []
        result = self.look_for_destination(nav_tree, self, destination)
        if result:
            return result
        else:
            return ""

    def look_for_destination(self, tree, location, destination):
        if location in tree.keys():
            for r in tree[location]:
                if r.name == destination:
                    return destination
                else:
                    t = self.look_for_destination(tree, r, destination)
                    if t:
                        try:
                            t.insert(0, r.name)
                        except AttributeError:
                            t = [r.name, t]
                        return t

    def generate_tree_level(self, tree, room, door_dict, checked):
        temp = room.get_adjacent(door_dict, checked)
        for t in temp:
            checked.append(t)
        tree[room] = temp
        return tree, checked

    def get_adjacent(self, door_dict, ignore=[]):
        results = []
        for door in self.doors:
            result = self.open_door(door_dict[door])
            if result != self and result not in ignore:
                results.append(result)
        return results

#We can add time to add a dificulty to some doors, say like the one to the treasure chest.
#and opening size, maybe the cat can't fit through some. We could also change the front and back room
#and create doors that go more than three places. A teleporter maybe?

class Door():
    def __init__(self,name, description, room1, room2, is_locked, key):
        self.name = name
        self.description = description
        self.front = room1
        self.back = room2
        self.is_locked = is_locked
        self.key = key

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def look(self):
        print(self.name + '\n' + self.description)

    def action(self, room ,player):
        if self.is_locked == True and player.inventory.check_inventory(self.key):
            print('The door is unlocked.')
            self.is_locked = False
        elif self.is_locked == False:
            print('The door is already unlocked')
        else:
            print('You need a key to unlock this door')
