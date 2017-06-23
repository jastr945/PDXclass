from random import choice

class Inventory:
    def __init__(self, owner):
        """The most complex object in this game is the inventory object as seen below.
        a full description of it's characteristics and functions can be found in the read
        me"""
        self.bag_of_holding = []
        self.owner = owner

    def put_in(self, item):
        """This method will add an item object to inventory, although"""
        try:
            self.bag_of_holding.append(item)
            print("You have added {} to your inventory.".format(item))
        except:
            print('Error in Inventory method: put_in')

    def put_in_quiet(self, item):
        """This method will add an item object to inventory, although"""
        try:
            self.bag_of_holding.append(item)
        except:
            print('Error in Inventory method: put_in')

    def check_inventory(self, check_word):
        """Quick method to check if an item exists in inventory, returns boolean
        value to call."""
        is_there = False
        for thing in self.bag_of_holding:
            if check_word == thing.name:
                is_there = True

        return is_there

    def look_for_type(self, t):
        results = []
        for i in self.bag_of_holding:
            if type(i) is t:
                results.append(i)
        if results:
            return choice(results)
        return ""

    def list_inventory(self):
        """Displays inventory of object to console, excludes spells that have been cast."""

        print('Your inventory contains:')
        #i = 1
        #inv_dict = {}
        for item in self.bag_of_holding:
            if 'casted' not in item.name:
                try:
                    print(item.name)
                except:
                    pass

                #inv_dict[str(i)] = item
                #i += 1
        #return inv_dict

    def poplar(self, item_to_be_popped):
        """Checks for existence of item in inventory, if item exists poplar pops that item and returns
        as als_lament"""
        if self.check_inventory(item_to_be_popped): # Basic check to see if it's in the list
            als_lament = item_to_be_popped# ;P
            for an_item in self.bag_of_holding:     # here we are extracting an the index of the object in the list
                if an_item.name == item_to_be_popped:
                    index = self.bag_of_holding.index(an_item)
                    to_be_returned = self.bag_of_holding[index]
            # and here is where the majic happens and the item is removed from the list.
            self.bag_of_holding.remove(self.bag_of_holding[index])
        else:
            # for testing porpoises if the item is not in dah bag, remove later.
            print(" {} was not found in bag of holding.".format(item_to_be_popped))
            return None
        return to_be_returned

    def look(self, item_to_be_described):
        """This method simply displays the description attached to an item when supplied
        with the item."""
        for item in self.bag_of_holding:
            if item_to_be_described == item.name:
                print('{}'.format(item.description))
